# UTF-8 Validation

## Description
This project is designed to implement a method to validate if a given list of integers represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. Each character in UTF-8 encoding can be represented by 1 to 4 bytes.

The `validUTF8` function checks that each integer in the list (representing 1 byte) follows the rules for valid UTF-8 encoding.

## Requirements
- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.4.3**
- **PEP 8** style (version 1.7.x) is used
- All files should end with a new line
- All files must be executable
- First line of each Python file: `#!/usr/bin/python3`

## Project Structure

- `0-validate_utf8.py`: Contains the `validUTF8(data)` function which validates UTF-8 encoding.
- `0-main.py`: Provides example usage of the `validUTF8` function for testing purposes.

## Function Prototype
```python
def validUTF8(data)
