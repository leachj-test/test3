"""
Test suite for the authentication system.
"""

import unittest
from auth import AuthSystem


class TestAuthSystem(unittest.TestCase):
    """Test cases for the AuthSystem class."""
    
    def setUp(self):
        """Set up a fresh AuthSystem instance for each test."""
        self.auth = AuthSystem()
        
    def test_register_user_success(self):
        """Test successful user registration."""
        result = self.auth.register_user("testuser", "testpass")
        self.assertTrue(result)
        self.assertIn("testuser", self.auth.users)
        
    def test_register_duplicate_user(self):
        """Test that duplicate usernames are rejected."""
        self.auth.register_user("testuser", "testpass")
        result = self.auth.register_user("testuser", "anotherpass")
        self.assertFalse(result)
        
    def test_signin_success(self):
        """Test successful sign in."""
        self.auth.register_user("testuser", "testpass")
        result = self.auth.signin("testuser", "testpass")
        self.assertTrue(result)
        self.assertTrue(self.auth.is_signed_in("testuser"))
        
    def test_signin_wrong_password(self):
        """Test sign in with incorrect password."""
        self.auth.register_user("testuser", "testpass")
        result = self.auth.signin("testuser", "wrongpass")
        self.assertFalse(result)
        self.assertFalse(self.auth.is_signed_in("testuser"))
        
    def test_signin_nonexistent_user(self):
        """Test sign in with non-existent user."""
        result = self.auth.signin("nonexistent", "testpass")
        self.assertFalse(result)
        
    def test_signin_already_signed_in(self):
        """Test signing in when already signed in."""
        self.auth.register_user("testuser", "testpass")
        self.auth.signin("testuser", "testpass")
        result = self.auth.signin("testuser", "testpass")
        self.assertTrue(result)  # Should still return True
        self.assertTrue(self.auth.is_signed_in("testuser"))
        
    def test_signout_success(self):
        """Test successful sign out."""
        self.auth.register_user("testuser", "testpass")
        self.auth.signin("testuser", "testpass")
        result = self.auth.signout("testuser")
        self.assertTrue(result)
        self.assertFalse(self.auth.is_signed_in("testuser"))
        
    def test_signout_not_signed_in(self):
        """Test sign out when user is not signed in."""
        self.auth.register_user("testuser", "testpass")
        result = self.auth.signout("testuser")
        self.assertFalse(result)
        
    def test_is_signed_in(self):
        """Test is_signed_in method."""
        self.auth.register_user("testuser", "testpass")
        self.assertFalse(self.auth.is_signed_in("testuser"))
        self.auth.signin("testuser", "testpass")
        self.assertTrue(self.auth.is_signed_in("testuser"))
        self.auth.signout("testuser")
        self.assertFalse(self.auth.is_signed_in("testuser"))
        
    def test_get_logged_in_users(self):
        """Test getting list of logged in users."""
        self.auth.register_user("user1", "pass1")
        self.auth.register_user("user2", "pass2")
        self.auth.register_user("user3", "pass3")
        
        self.assertEqual(len(self.auth.get_logged_in_users()), 0)
        
        self.auth.signin("user1", "pass1")
        self.assertEqual(len(self.auth.get_logged_in_users()), 1)
        self.assertIn("user1", self.auth.get_logged_in_users())
        
        self.auth.signin("user2", "pass2")
        self.assertEqual(len(self.auth.get_logged_in_users()), 2)
        self.assertIn("user1", self.auth.get_logged_in_users())
        self.assertIn("user2", self.auth.get_logged_in_users())
        
        self.auth.signout("user1")
        self.assertEqual(len(self.auth.get_logged_in_users()), 1)
        self.assertNotIn("user1", self.auth.get_logged_in_users())
        self.assertIn("user2", self.auth.get_logged_in_users())
        
    def test_multiple_users(self):
        """Test multiple users signing in and out."""
        # Register users
        self.auth.register_user("alice", "pass1")
        self.auth.register_user("bob", "pass2")
        self.auth.register_user("charlie", "pass3")
        
        # Sign in all users
        self.auth.signin("alice", "pass1")
        self.auth.signin("bob", "pass2")
        self.auth.signin("charlie", "pass3")
        
        # Verify all are signed in
        logged_in = self.auth.get_logged_in_users()
        self.assertEqual(len(logged_in), 3)
        self.assertIn("alice", logged_in)
        self.assertIn("bob", logged_in)
        self.assertIn("charlie", logged_in)
        
        # Sign out one user
        self.auth.signout("bob")
        logged_in = self.auth.get_logged_in_users()
        self.assertEqual(len(logged_in), 2)
        self.assertIn("alice", logged_in)
        self.assertNotIn("bob", logged_in)
        self.assertIn("charlie", logged_in)


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
