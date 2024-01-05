import toml


def parse_envs_from_toml(file_path):
    try:
        # Load and parse the TOML file
        data = toml.load(file_path)

        # Extract the 'envs' section
        envs = data.get("tool", {}).get("easyenv", {}).get("envs", [])

        # Print details of each env
        for env in envs:
            name = env.get("name", "N/A")
            description = env.get("description", "No description provided")
            help_text = env.get("help", "No help text provided")
            print(
                f"Name: {name}, Description: {description}, Help: {help_text}")
    except Exception as e:
        print(f"Error reading the TOML file: {e}")


if __name__ == "__main__":
    # Replace with your actual file path
    toml_file_path = 'pyproject.toml'
    parse_envs_from_toml(toml_file_path)
