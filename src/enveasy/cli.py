import typer
import os
from pathlib import Path
from enveasy.utils import init_enveasy, add_enveasy, export_variable_data, setup_env, export_env_example
from rich import print
from rich.prompt import Prompt
app = typer.Typer()


@app.command()
def init():
    path = os.path.join(os.getcwd(), "enveasy.toml")
    if os.path.exists(path):
        print(
            "[bold red]enveasy.toml already exists[/bold red], use [bold yellow] enveasy add [/bold yellow] to add enviroment variables")
        raise typer.Exit()
    else:
        confirm = typer.confirm(
            "Are you sure you want to initialize enveasy.toml?", abort=True)
        print("[green]Initializing enveasy.toml[/green] :boom:")
        init_enveasy()
        print(
            "[bold green]Done[/bold green] :sparkles:, Use [bold yellow] enveasy add [/bold yellow]to add enviroment variables")


@app.command()
def add():
    path = os.path.join(os.getcwd(), "enveasy.toml")
    if not os.path.exists(path):
        print(
            "[bold red]enveasy is not initialize :see_no_evil:[/bold red], use [bold yellow] enveasy init [/bold yellow] to initalize enveasy")
        raise typer.Exit()
    else:
        while True:
            variable_name = Prompt.ask("Enter your variable name :sunglasses:")
            variable_description = Prompt.ask(
                "Enter your variable description :sunglasses:")
            variable_help = Prompt.ask(
                "Enter your variable help :sunglasses:")
            add_enveasy(variable_name, variable_description, variable_help)
            print("Done")
            confirm = typer.confirm(
                "Do you want to add more variables?", abort=True)


@app.command()
def set():
    path = os.path.join(os.getcwd(), ".env")
    if not os.path.exists(path):
        with open(".env", 'w') as f:
            f.write("")
    environment_var_data = export_variable_data()
    for i in environment_var_data:
        print("Description: ", i[1])
        print("Help: ", i[2])
        value = input(f"Please Enter the Value of {i[0]}: ")
        setup_env(i[0], value)


@app.command()
def export():
    path = os.path.join(os.getcwd(), ".env_example")
    if not os.path.exists(path):
        with open(".env_example", 'w') as f:
            f.write("")
    environment_var_data = export_variable_data()
    for i in environment_var_data:
        export_env_example(i[0], i[1])
    print("[bold green]Done exporting[/bold green][yellow] .env_example [/yellow] :sparkles:,")


if __name__ == "__main__":
    app()
