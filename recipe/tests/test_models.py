from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUserModel(TestCase):

    # test creation of user with custom user model
    def test_create_user_with_email(self):
        #variable for username email
        email = 'test@example.com'
        #variable for username password
        password = "tester123"
        #create user
        user = get_user_model().objects.create_user(email=email, password=password)

        #now we can assert that the user was created correctly
        #assert that instance user.email == email assigned in function
        self.assertEqual(user.email, email)

        #check that instance user.password == password assigned in function
        self.assertTrue(user.check_password(password))