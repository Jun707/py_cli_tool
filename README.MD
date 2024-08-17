# Miso

Miso is a CLI tool designed to help optimize your workflow by saving frequently used URL paths and grouping different URLs for easy access. It allows you to store, manage, and quickly open your most visited websites or web applications directly from the command line.

## Features

- **Store URLs**: Save frequently used URLs into a local text file for quick access.
- **Open URLs**: Open all stored URLs in your default web browser with a single command.
- **List URLs**: View all stored URLs directly in the terminal.
- **Remove URLs**: Delete specific URLs from the stored list.
- **Validation**: Ensure that only valid domain URLs are stored.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Jun707/py_cli_tool
    ```

2. Navigate to the project directory:
    ```bash
    cd py_cli_tool
    ```

3. Install the package using `pip`:
    ```bash
    pip install .
    ```

4. Export your browser path if needed (optional):
    ```bash
    export BROWSER=/mnt/c/Program\ Files/Google/Chrome/Application/chrome.exe
    ```

## Usage

After installing `miso`, you can use the following commands:

### Open all stored url paths
```bash
miso read
```

### Read stored url paths
```bash
miso read -ls
```

### Save a URL
To save a new URL:

```bash
miso save <url>
```

### Remove a URL
```bash
miso rm <url>
```

## Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request. When contributing, please ensure that your code follows the project's coding standards and that all tests pass.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.

## Author

Miso was created by Junwen Huang. If you have any questions or feedback, feel free to reach out via email: [juntowork@gmail.com](mailto:juntowork@gmail.com).
