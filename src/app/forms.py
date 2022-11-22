import string
from typing import List
from rich import print
import os
from .common import get_base, include

dir_path = os.path.dirname(os.path.realpath(__file__))

CONTEXT = {
    "include_labels": False,
    "include_placeholders": False,
    "include_validation": True,
}


class Field:
    def __init__(self, name, type) -> None:
        self.name = name
        if type:
            self.input_type = type
        else:
            self.input_type = "text"

        self.type = self.get_type()
        self.initial_value = self.get_initial_value()

    def get_type(self):
        match self.input_type:
            case "text":
                return "string"
            case "email":
                return "string"
            case "number":
                return "number"
            case "pass":
                self.input_type = "password"
                return "string"
            case "date":
                return "Date"

    def get_initial_value(self):
        match self.type:
            case "string":
                return "''"
            case "number":
                return "0"
            case "Date":
                return "new Date()"


def fields_to_jsx(fields: List[Field]) -> str:
    jsx_list = []
    for field in fields:
        line = (
            include(
                f'<label htmlFor="{field.name}">{field.name.capitalize()}</label>\n\t\t\t\t\t'
            ).when(CONTEXT["include_labels"])
            + f'<Field id="{field.name}" type="{field.input_type}" name="{field.name}"'
            + include(f' placeholder="{field.name}"').when(
                CONTEXT["include_placeholders"]
            )
            + " />"
            + include(
                "\n\t\t\t\t\t{errors."
                + field.name
                + " && touched."
                + field.name
                + " ? (\n\t\t\t\t\t\t<div>{errors."
                + field.name
                + "}</div>\n\t\t\t\t\t) : null}"
            ).when(CONTEXT["include_errors"])
        )
        jsx_list.append(line)
    return "\n\t\t\t\t\t".join(jsx_list)


def fields_to_interface(fields: List[Field]) -> str:
    types_list = []
    for field in fields:
        line = f"{field.name}: {field.type}"
        types_list.append(line)
    return "\n    ".join(types_list)


def fields_to_values(fields: List[Field]) -> str:
    types_list = []
    for field in fields:
        line = f"{field.name}: {field.initial_value}"
        types_list.append(line)
    return ",\n\t\t\t\t\t".join(types_list)


def generate_validation_schema(fields: List[Field], name: str) -> str:
    fields_string = []
    base = """
const CadastroSchema = Yup.object().shape({
    %FIELDS%
});\n"""

    for field in fields:
        fields_string.append(f"{field.name}: Yup.{field.type.lower()}(),\n\t")

    fields_string[-1] = fields_string[-1][:-3]

    return base.replace("%FIELDS%", "".join(fields_string))


def generate_form(
    name: str,
    _fields: str,
    include_label: bool,
    include_placeholder: bool,
    include_validation: bool,
    include_errors: bool,
):

    CONTEXT["include_labels"] = include_label
    CONTEXT["include_placeholders"] = include_placeholder
    CONTEXT["include_validation"] = include_validation
    CONTEXT["include_errors"] = include_errors

    fields = []
    for field in _fields.split(","):
        field = field.split(":")
        fields.append(Field(name=field[0], type=field[1] if 1 < len(field) else None))

    content = (
        get_base(f"{dir_path}/../bases/Form.txt")
        .replace("%FORM_NAME%", name.capitalize())
        .replace("%INPUTS_JSX%", fields_to_jsx(fields))
        .replace("%INPUTS_INTERFACE%", fields_to_interface(fields))
        .replace("%INITIAL_VALUES%", fields_to_values(fields))
        .replace(
            "%VALIDATION_JSX%",
            include(
                f'\n\t\t\t\tvalidationSchema={"{" + name.capitalize() + "Schema}"}'
            ).when(CONTEXT["include_validation"]),
        )
        .replace(
            "%YUP_IMPORT%",
            include("import * as Yup from 'yup';").when(CONTEXT["include_validation"]),
        )
        .replace(
            "%VALIDATION_SCHEMA%",
            include(generate_validation_schema(fields, name)).when(
                CONTEXT["include_validation"]
            ),
        )
        .replace(
            "%ERRORS_CLOSE_CALLBACK%",
            include("\n\t\t\t\t)}").when(CONTEXT["include_errors"]),
        )
        .replace(
            "%ERRORS_OPEN_CALLBACK%",
            include("\n\t\t\t\t{({ errors, touched }) => (").when(
                CONTEXT["include_errors"]
            ),
        )
    )

    filename = f"./src/forms/{name.capitalize()}.tsx"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[green]Generated file [bold]{filename}[/bold] with success.[/green]")
