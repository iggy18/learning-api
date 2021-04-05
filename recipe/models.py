from django.db import models
from django.contrib.auth. models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user.
        """
        #pass email first then pass anything extra we add
        user = self.model(email=email, **extra_fields)
        #always use SET password to store the password so it's encrypted
        user.set_password(password)

        #saves the user
        user.save(using=self._db)

        #returns the user
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ 
    custom user model that supports using email instead of username
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    #user is not staff.
    is_staff = models.BooleanField(default=False)

    #creates a new user manager
    objects = UserManager()

    USERNAME_FIELD = 'email'