import typer
from rich import print
from app import forms

app = typer.Typer(name="mkg")


@app.command()
def form(name: str, fields: str):
    """
    Generates a form component in the src/forms directory.
    You pass the fields separated by a comma, and specify which type they will
    have in the HTML input. The type text can be omitted, as it is the most used.
    Usage: mkg form cadastro name,email:email,idade:number,nascimento:date
    """
    forms.generate_form(name, fields)


@app.command()
def test(name: str):
    """prints your name"""
    print(name)


if __name__ == "__main__":
    app()
