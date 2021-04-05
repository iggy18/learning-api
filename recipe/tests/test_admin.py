from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

#tests for the admin site. since we changed the user model we want to test the admin site
class AdminSiteTests(TestCase):
    
    #set up fucntion is run before every test in test case class
    def setUp(self):
        self.client = Client()
        #create superuser
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@example.com',
            password = 'hello12345',
        )
        
        self.client.force_login(self.admin_user)

        #create regular user
        self.user = get_user_model().objects.create_user(
            email = "other@example.com",
            password = 'hello15',
            name = 'lee scoresby'
        )
    
    ####tests####
    def test_users_listed(self):
        """ test that users are listed on user page """
        url = reverse('admin:recipe_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_change_page_renders_correctly(self):
        """test that the user edit page works"""
        url = reverse('admin:recipe_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_add_page_renders_correctly(self):
        url = reverse('admin:recipe_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
