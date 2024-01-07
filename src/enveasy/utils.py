from configparser import ConfigParser
import toml
import os
from enveasy.config import DEFAULT_ENV_FILE, DEFAULT_TOML_FILE, DEFAULT_EXPORT_FILE


def pyproject_toml_exists():
    pyproject_path = os.path.join(os.getcwd(), "pyproject.toml")
    if os.path.exists(pyproject_path):
        return True
    return False


def find_toml_file():
    enveasy_toml_path = os.path.join(os.getcwd(), DEFAULT_TOML_FILE)
    if pyproject_toml_exists():
        pyproject_path = os.path.join(os.getcwd(), "pyproject.toml")
        data = toml.load(pyproject_path)
        if "tool" in data and "enveasy" in data["tool"]:
            return "pyproject.toml"
    if os.path.exists(enveasy_toml_path):
        return DEFAULT_TOML_FILE
    return None


def init_enveasy(file_path=DEFAULT_TOML_FILE):
    config = ConfigParser()
    config["tool.enveasy"] = {
    }
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


def export_variable_data():

    # Path to your TOML file
    file_path = DEFAULT_TOML_FILE

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
    with open(DEFAULT_ENV_FILE, "a") as f:
        f.write(f'{variable_name}="{variable_value}"\n')


def export_env_example(variable_name, variable_description):
    with open(DEFAULT_EXPORT_FILE, "a") as f:
        f.write(f'{variable_name}="{variable_description}"\n')
