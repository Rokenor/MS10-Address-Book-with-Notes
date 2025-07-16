# MS10-Address-Book-with-Notes

A command-line address book application with birthday tracking and contact management features.

## Features

- Add, edit, and delete contacts
- Store phone numbers with validation
- Birthday tracking and reminders
- Persistent data storage using pickle
- Input validation and error handling
- Command-line interface
- Notes taking features

## Python Version Requirements

**Recommended Python Version: 3.8+**

- **Minimum Required**: Python 3.6
- **Recommended**: Python 3.8 or higher

## Installation

### Method 1: Install from Source (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rokenor/MS10-Address-Book-with-Notes.git
   ```
   ```bash
   cd MS10-Address-Book-with-Notes
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```
   ```bash
   source venv/bin/activate
   

3. **Install the package:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation, run the application:

```bash
python main.py
```

### Example Usage

```
Enter a command: add John 1234567890
Contact added.

Enter a command: add-birthday John 15.03.1990
Birthday added.

Enter a command: phone John
Contact name: John, phones: 1234567890

Enter a command: all
Contact name: John, phones: 1234567890
```

## Troubleshooting

### Common Issues

1. **Python version compatibility**: Ensure you're using Python 3.6+
2. **Module import errors**: Make sure you're running from the correct directory
3. **Permission errors**: Use virtual environments to avoid system-wide installations

### Virtual Environment Issues

If you encounter issues with virtual environments:

```bash
# Remove existing virtual environment
rm -rf .venv

# Create new virtual environment
python -m venv .venv
source venv/bin/activate
pip install -r requirements.txt
```

## Data Storage

The application stores data in `storage/addressbook.pkl`. This file is automatically created when you first add a contact.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source.
## Support

For issues and questions, please create an issue in the GitHub repository.
