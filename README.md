# enveasy

**enveasy** is a command-line tool designed to easily manage environment variables within your projects. It allows you to initialize configuration files, add environment variables, set their values, and export example environment files.

## Features

- Initialize `enveasy` configuration in `pyproject.toml` or `enveasy.toml`.
- Add environment variables with descriptions and help text.
- Set environment variable values interactively.
- Export environment variables to an example `.env_example` file.

## Requirements

- Python 3.9 or higher
- Dependencies: `typer`, `rich`, `tomli`, `toml`, `setuptools`, `wheel`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/enveasy.git
   cd enveasy
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Commands

- **Initialize `enveasy` Configuration**

  ```bash
  enveasy init
  ```

  This command initializes the `enveasy` configuration. It will either add the configuration to `pyproject.toml` or create a new `enveasy.toml` file.

- **Add Environment Variables**

  ```bash
  enveasy add
  ```

  This command allows you to add environment variables interactively, providing a name, description, and help text for each variable.

- **Set Environment Variable Values**

  ```bash
  enveasy set
  ```

  This command prompts you to enter values for the environment variables defined in the configuration file.

- **Export Environment Variables Example**

  ```bash
  enveasy export
  ```

  This command exports the environment variables and their descriptions to an example file (`.env_example`).

## Project Structure

- `pyproject.toml`: Contains project metadata, dependencies, and build system requirements.
- `__init__.py`: Initializes the `enveasy` package.
- `cli.py`: Defines the CLI commands using `typer`.
- `config.py`: Defines default filenames used throughout the project.
- `parser.py`: Script to parse environment variables from a TOML file.
- `utils.py`: Utility functions for various tasks such as initializing configuration, adding variables, and exporting data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
