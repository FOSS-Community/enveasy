import typer
import os
from pathlib import Path
from enveasy.utils import init_enveasy, add_enveasy, export_variable_data, setup_env, export_env_example, pyproject_toml_exists, find_initialised_toml_file
from rich import print
from rich.prompt import Prompt
from enveasy.config import DEFAULT_ENV_FILE, DEFAULT_TOML_FILE
app = typer.Typer()


@app.command()
def init():
    if pyproject_toml_exists():
        print("[bold green]Found pyproject.toml[/bold green] :sparkles:")
        confirm = typer.confirm(
            "Do you want to add enveasy to pyproject.toml?", default=True)
        if confirm:
            init_enveasy("pyproject.toml")
            print(
                "[bold green]Done[/bold green] :sparkles:, Use [bold yellow] enveasy add [/bold yellow]to add enviroment variables")
            return
    path = os.path.join(os.getcwd(), DEFAULT_TOML_FILE)
    if os.path.exists(path):
        print(
            "[bold red]enveasy.toml already exists[/bold red], use [bold yellow] enveasy add [/bold yellow] to add enviroment variables")
        raise typer.Exit()
    else:
        confirm = typer.confirm(
            "Are you sure you want to initialize enveasy.toml?", abort=True, default=True)
        print("[green]Initializing enveasy.toml[/green] :boom:")
        init_enveasy()
        print(
            "[bold green]Done[/bold green] :sparkles:, Use [bold yellow] enveasy add [/bold yellow]to add enviroment variables")


@app.command()
def add():
    path = os.path.join(os.getcwd(), file := find_initialised_toml_file())
    if not os.path.exists(path):
        print(
            "[bold red]enveasy is not initialize :see_no_evil:[/bold red], use [bold yellow] enveasy init [/bold yellow] to initalize enveasy")
        raise typer.Exit()
    else:
        while True:
            variable_name = ""
            while not variable_name:
                variable_name = Prompt.ask(
                    "Enter your variable name :sunglasses:")
                if variable_name == "":
                    print("[bold red]Please enter a variable name[/bold red]")
            variable_description = Prompt.ask(
                "Enter your variable description :sunglasses:")
            variable_help = Prompt.ask(
                "Enter your variable help :sunglasses:")
            add_enveasy(variable_name, variable_description,
                        variable_help, file)
            print("Done")
            confirm = typer.confirm(
                "Do you want to add more variables?", abort=True)


@app.command()
def set(env_file=DEFAULT_ENV_FILE):
    path = os.path.join(os.getcwd(), env_file)
    if not os.path.exists(path):
        with open(env_file, 'w') as f:
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
