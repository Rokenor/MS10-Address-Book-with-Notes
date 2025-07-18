# MS10-Address-Book-with-Notes

A comprehensive command-line contact management system with integrated notes functionality. This application helps you organize your contacts, track important dates, and manage notes efficiently.

## Features

- Comprehensive contact management:
  - Add, edit, and delete contacts
  - Store multiple phone numbers (displayed as comma-separated strings)
  - Manage email addresses with validation
  - Track physical addresses with improved display
  - Birthday tracking and reminders

- Advanced notes system:
  - Create and manage notes with dividers for better readability
  - Add tags for organization
  - Search notes by content or tags
  - Sort notes by tags
  - Edit and delete notes

- Enhanced UI:
  - Colorized output for better visibility
    - Green text for success messages
    - Red text for errors and warnings
  - Themed tables with improved formatting
  - Clear dividers between notes for better organization
  - Better formatting for phone numbers and addresses

- Persistent data storage:
  - Automatic data persistence using pickle
  - Separate storage for contacts and notes
  - Data backup and recovery

- User-friendly interface:
  - Command-based interaction with color-coded prompts
  - Input validation with colored error messages
  - Help system with command descriptions
  - Interactive prompts for better user experience

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
# Contact Management
Enter a command: add John 1234567890
Contact added.

Enter a command: add-birthday John 15.03.1990
Birthday added.

Enter a command: add-email John john@example.com
Email added.

# Notes Management
Enter a command: note Important work meeting
Note created.

Enter a command: note-search meeting
Found notes: work meeting

Enter a command: note-tag-sort
Notes sorted by tags
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

The application uses two separate storage files:

- `storage/addressbook.pkl`: Stores contact information
- `storage/notes.pkl`: Stores notes and tags

These files are automatically created when you first add a contact or note.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source.
## Support

For issues and questions, please create an issue in the GitHub repository.
