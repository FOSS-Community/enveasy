from configparser import ConfigParser
import toml
import os
from enveasy.config import DEFAULT_ENV_FILE, DEFAULT_TOML_FILE, DEFAULT_EXPORT_FILE
from rich import print


def pyproject_toml_exists():
    """
    Check if pyproject.toml exists in root directory of project
    """
    pyproject_path = os.path.join(os.getcwd(), "pyproject.toml")
    if os.path.exists(pyproject_path):
        return True
    return False


def find_initialised_toml_file():
    """
    Used to find the toml file, if enveasy.toml exists, then it will be used, else if pyproject.toml exists, then it will be used, else None will be returned
    Also gives information if project is initialised or not
    """
    enveasy_toml_path = os.path.join(os.getcwd(), DEFAULT_TOML_FILE)
    if os.path.exists(enveasy_toml_path):
        return DEFAULT_TOML_FILE
    if pyproject_toml_exists():
        pyproject_path = os.path.join(os.getcwd(), "pyproject.toml")
        data = toml.load(pyproject_path)
        if "tool" in data and "enveasy" in data["tool"]:
            return "pyproject.toml"
    return None


def init_enveasy(file_path=DEFAULT_TOML_FILE):
    if file := find_initialised_toml_file():
        print(
            "[bold red]enveasy is already initialized :see_no_evil:[/bold red], use [bold yellow] enveasy add [/bold yellow] to add enviroment variables")
        print(
            f"enveasy is already initialized in \"{file}\"")
        exit(1)
    config = ConfigParser()
    config["tool.enveasy"] = {
    }
    if file_path == "pyproject.toml":
        with open(file_path, "a") as f:
            config.write(f)
    else:
        with open(file_path, "w") as f:
            config.write(f)


def add_enveasy(variable_name, variable_description, variable_help, file_path=DEFAULT_TOML_FILE):
    # Path to your TOML file

    # Read the existing TOML file
    with open(file_path, 'r') as file:
        data = toml.load(file)

    # Modify the data
    # Check if 'tool.enveasy' section exists, and add or modify 'varname'
    if 'tool' in data and 'enveasy' in data['tool']:
        data['tool']['enveasy'][variable_name] = [
            variable_description, variable_help]
    else:
        print("Section [tool.enveasy] not found in the TOML file.")

    # Write the changes back to the file
    with open(file_path, 'w') as file:
        toml.dump(data, file)


def export_variable_data(file_path=find_initialised_toml_file()):

    # Read the TOML file
    with open(file_path, 'r') as file:
        data = toml.load(file)

    # Initialize an empty list to store the configuration data
    export_config_data = []

    # Check and process the 'tool.enveasy' section
    if 'tool' in data and 'enveasy' in data['tool']:
        for var_name, values in data['tool']['enveasy'].items():
            # Assuming each variable has at least two elements: description and help
            if len(values) >= 2:
                # Append a tuple with the variable name, description, and help text
                export_config_data.append((var_name, values[0], values[1]))
            else:
                print(f"Insufficient data for variable '{var_name}'")
    else:
        print("Section [tool.enveasy] not found in the TOML file.")

    # Print the export_config_data list
    return export_config_data


def setup_env(variable_name, variable_value):
    env_file_path = DEFAULT_ENV_FILE
    # Read existing lines from the environment file
    with open(env_file_path, 'r') as f:
        lines = f.readlines()
    # Check if the variable_name already exists in the file
    variable_exists = any(line.startswith(
        f"{variable_name}=") for line in lines)
    # If the variable_name exists, replace the existing line; otherwise, add a new line
    if variable_exists:
        updated_lines = [f"{variable_name}={variable_value}\n" if line.startswith(
            f"{variable_name}=") else line for line in lines]
    else:
        updated_lines = lines + [f"{variable_name}={variable_value}\n"]
    # Write the updated lines back to the environment file
    with open(env_file_path, 'w') as f:
        f.writelines(updated_lines)


def export_env_example(variable_name, variable_description):
    export_file = DEFAULT_EXPORT_FILE
    with open(export_file, 'r') as f:
        lines = f.readlines()
    # Check if the variable_name already exists in the file
    variable_exists = any(line.startswith(
        f"{variable_name}=") for line in lines)
    # If the variable_name exists, replace the existing line; otherwise, add a new line
    if variable_exists:
        updated_lines = [f"{variable_name}={variable_description}\n" if line.startswith(
            f"{variable_name}=") else line for line in lines]
    else:
        updated_lines = lines + [f"{variable_name}={variable_description}\n"]
    # Write the updated lines back to the environment file
    with open(export_file, 'w') as f:
        f.writelines(updated_lines)
