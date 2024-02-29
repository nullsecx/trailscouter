# TrailScouter

TrailScouter is a tool for collecting subdomains from SecurityTrails and performing DNS history enumeration. It provides a simple and efficient way to gather information about a domain's subdomains and its historical DNS records.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/trailscouter.git
    ```

2. Navigate to the project directory:

    ```
    cd trailscouter
    ```

3. Install the required Python dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Obtain your SecurityTrails API key from [SecurityTrails](https://securitytrails.com/).
2. Store your API key in a file named `securitytrails_api_key.txt` in the project directory.
3. Run the `trailscouter.py` script:

    ```
    python trailscouter.py
    ```

4. Follow the prompts to enter the domain for which you want to collect subdomains and the name of the output file.
5. The tool will collect subdomains from SecurityTrails and write them to the specified output file.

## Advantages

- Simple and intuitive command-line interface.
- Utilizes SecurityTrails API for accurate and up-to-date subdomain information.
- Can be easily extended to include additional features such as DNS history enumeration.
- Lightweight and easy to install with minimal dependencies.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
