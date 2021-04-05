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


    def test_new_user_email_is_normalized(self):
        email = 'test@EXAMPLE.com'
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())


    def test_create_user_with_email_no_email_raises_error(self):
        #test that whatever you run in the funciton below raises the specified error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')


    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(email='test@example.com', password='testertest1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)