import toml


def parse_envs_from_toml(file_path, debug=False):
    try:
        # Load and parse the TOML file
        data = toml.load(file_path)

        # Extract the 'envs' section
        envs = data.get("tool", {}).get("enveasy", {})
        if debug:
            print(f"Found {len(envs)} envs")

        # Print details of each env
        for env in envs:
            name = env
            description = envs[env][0] if envs[env][0] else "No description provided"
            help_text = envs[env][1] if envs[env][1] else "No help provided"
            print(
                f"Name: {name}, Description: {description}, Help: {help_text}")
    except Exception as e:
        print(f"Error reading the TOML file: {e}")


if __name__ == "__main__":
    # Replace with your actual file path
    toml_file_path = 'pyproject.toml'
    parse_envs_from_toml(toml_file_path, debug=True)
