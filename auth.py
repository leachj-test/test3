"""
Simple authentication system with signin and signout functionality.
"""

class AuthSystem:
    """A simple authentication system for managing user sessions."""
    
    def __init__(self):
        """Initialize the authentication system."""
        self.users = {}  # username: password
        self.logged_in_users = set()  # currently logged in users
        
    def register_user(self, username, password):
        """
        Register a new user in the system.
        
        Args:
            username (str): The username to register
            password (str): The password for the user
            
        Returns:
            bool: True if registration successful, False if user already exists
        """
        if username in self.users:
            return False
        self.users[username] = password
        return True
    
    def signin(self, username, password):
        """
        Sign in a user to the system.
        
        Args:
            username (str): The username to sign in
            password (str): The password for authentication
            
        Returns:
            bool: True if signin successful, False otherwise
        """
        if username not in self.users:
            print(f"Error: User '{username}' does not exist.")
            return False
            
        if self.users[username] != password:
            print(f"Error: Incorrect password for user '{username}'.")
            return False
            
        if username in self.logged_in_users:
            print(f"Warning: User '{username}' is already signed in.")
            return True
            
        self.logged_in_users.add(username)
        print(f"Success: User '{username}' signed in successfully.")
        return True
    
    def signout(self, username):
        """
        Sign out a user from the system.
        
        Args:
            username (str): The username to sign out
            
        Returns:
            bool: True if signout successful, False otherwise
        """
        if username not in self.logged_in_users:
            print(f"Error: User '{username}' is not currently signed in.")
            return False
            
        self.logged_in_users.remove(username)
        print(f"Success: User '{username}' signed out successfully.")
        return True
    
    def is_signed_in(self, username):
        """
        Check if a user is currently signed in.
        
        Args:
            username (str): The username to check
            
        Returns:
            bool: True if user is signed in, False otherwise
        """
        return username in self.logged_in_users
    
    def get_logged_in_users(self):
        """
        Get a list of all currently logged in users.
        
        Returns:
            list: List of usernames currently signed in
        """
        return list(self.logged_in_users)


def main():
    """Demo of the authentication system."""
    auth = AuthSystem()
    
    # Register some users
    print("=== Registering Users ===")
    auth.register_user("alice", "password123")
    auth.register_user("bob", "securepass")
    print("Users registered: alice, bob\n")
    
    # Sign in users
    print("=== Sign In ===")
    auth.signin("alice", "password123")
    auth.signin("bob", "securepass")
    print()
    
    # Check logged in users
    print("=== Logged In Users ===")
    print(f"Currently logged in: {auth.get_logged_in_users()}\n")
    
    # Sign out a user
    print("=== Sign Out ===")
    auth.signout("alice")
    print()
    
    # Check logged in users again
    print("=== Logged In Users ===")
    print(f"Currently logged in: {auth.get_logged_in_users()}\n")
    
    # Try to sign in with wrong password
    print("=== Failed Sign In Attempt ===")
    auth.signin("bob", "wrongpassword")
    print()
    
    # Sign out remaining user
    print("=== Sign Out Remaining User ===")
    auth.signout("bob")
    print()
    
    # Final status
    print("=== Final Status ===")
    print(f"Currently logged in: {auth.get_logged_in_users()}")


if __name__ == "__main__":
    main()
