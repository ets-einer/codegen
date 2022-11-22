#!/usr/bin/env python

import typer
from rich import print
from app import forms, pages

app = typer.Typer(name="mkg")


@app.command()
def form(
    name: str,
    fields: str,
    label: bool = typer.Option(
        False, help="Specifies if labels should be included or not"
    ),
    placeholder: bool = typer.Option(
        False, help="Specifies if placeholders should be included or not"
    ),
    validation: bool = typer.Option(
        True, help="Specifies if Yup validation should be included or not"
    ),
    errors: bool = typer.Option(
        False, help="Specifies if yup validation errors should be included or not"
    ),
):
    """
    Generates a form component in the src/forms directory.
    You pass the fields separated by a comma, and specify which type they will
    have in the HTML input. The type text can be omitted, as it is the most used.
    Usage: mkg form cadastro name,email:email,idade:number,nascimento:date
    """
    forms.generate_form(name, fields, label, placeholder, validation, errors)


@app.command()
def page(
    name: str,
    route: bool = typer.Option(
        False, help="Specifies if a different route component should be generated too."
    ),
):
    """
    Generates a page component in the src/pages directory.
    Usage: mkg page login
    """
    pages.generate_page(name, route)


@app.command()
def component(name: str):
    """
    Generates a component in the src/components directory.
    Usage: mkg component footer
    """
    pass


if __name__ == "__main__":
    app()
