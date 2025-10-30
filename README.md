# Authentication System

A simple, lightweight authentication system implementing signin and signout functionality.

## Overview

This project provides a basic authentication system that allows users to:
- **Sign in** to the system with username and password
- **Sign out** from the system
- Register new users
- Track currently logged-in users

## Features

- ✅ **User Registration**: Register new users with username and password
- ✅ **Sign In**: Authenticate users with their credentials
- ✅ **Sign Out**: Securely log out users from the system
- ✅ **Session Management**: Track which users are currently signed in
- ✅ **Error Handling**: Proper error messages for invalid operations

## Installation

No external dependencies are required! This system uses only Python standard library.

### Requirements

- Python 3.6 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/leachj-test/test3.git
cd test3
```

2. Run the demo:
```bash
python auth.py
```

## Usage

### Basic Example

```python
from auth import AuthSystem

# Create an authentication system
auth = AuthSystem()

# Register a new user
auth.register_user("john_doe", "secure_password")

# Sign in
auth.signin("john_doe", "secure_password")
# Output: Success: User 'john_doe' signed in successfully.

# Check if user is signed in
if auth.is_signed_in("john_doe"):
    print("User is logged in!")

# Sign out
auth.signout("john_doe")
# Output: Success: User 'john_doe' signed out successfully.
```

### API Reference

#### `AuthSystem()`

Create a new authentication system instance.

#### `register_user(username, password)`

Register a new user in the system.

**Parameters:**
- `username` (str): The username to register
- `password` (str): The password for the user

**Returns:**
- `bool`: True if registration successful, False if user already exists

#### `signin(username, password)`

Sign in a user to the system.

**Parameters:**
- `username` (str): The username to sign in
- `password` (str): The password for authentication

**Returns:**
- `bool`: True if signin successful, False otherwise

#### `signout(username)`

Sign out a user from the system.

**Parameters:**
- `username` (str): The username to sign out

**Returns:**
- `bool`: True if signout successful, False otherwise

#### `is_signed_in(username)`

Check if a user is currently signed in.

**Parameters:**
- `username` (str): The username to check

**Returns:**
- `bool`: True if user is signed in, False otherwise

#### `get_logged_in_users()`

Get a list of all currently logged in users.

**Returns:**
- `list`: List of usernames currently signed in

## Demo

Run the included demo to see the authentication system in action:

```bash
python auth.py
```

This will demonstrate:
- User registration
- Successful sign in
- Viewing logged in users
- Sign out functionality
- Failed login attempts
- Error handling

## Testing

Run the test suite to verify functionality:

```bash
python test_auth.py
```

## Architecture

The authentication system is built with simplicity and clarity in mind:

- **AuthSystem Class**: Main class managing authentication operations
- **User Storage**: In-memory dictionary storing user credentials
- **Session Management**: Set-based tracking of logged-in users
- **Error Handling**: Clear error messages for debugging

## Security Considerations

⚠️ **Note**: This is a demonstration project for learning purposes. In production environments:

- **Never store passwords in plain text** - use proper password hashing (e.g., bcrypt, argon2)
- **Use HTTPS** - protect credentials in transit
- **Implement rate limiting** - prevent brute force attacks
- **Add session timeouts** - automatically log out inactive users
- **Use secure session tokens** - instead of username-based sessions
- **Enable multi-factor authentication** - add an extra layer of security

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created as a demonstration of basic authentication concepts.

## Support

For issues, questions, or contributions, please open an issue on GitHub.
