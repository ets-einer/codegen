from rich import print
from .common import get_base, include
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

route_component_base = """const %PAGE_NAME%Route = () => {

    return <%PAGE_NAME%Page />;
}"""


def generate_page(name: str, is_route: bool):
    name = name.capitalize()

    def get_default_export():
        if is_route:
            return name + "Route"
        return name + "Page"

    content = (
        get_base(f"{dir_path}/../bases/Page.txt")
        .replace("%PAGE_NAME%", name)
        .replace(
            "%ROUTE_COMPONENT%",
            include(route_component_base.replace("%PAGE_NAME%", name)).when(is_route),
        )
        .replace("%EXPORT_DEFAULT%", get_default_export())
    )

    filename = f"./src/pages/{name}.tsx"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[green]Generated file [bold]{filename}[/bold] with success.[/green]")
