from django.db import models
from django.contrib.auth. models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user.
        """
        if not email:
            raise ValueError("Email address is required")

        #pass email first then pass anything extra we add normalize makes email lowercase
        user = self.model(email=self.normalize_email(email), **extra_fields)
        #always use SET password to store the password so it's encrypted
        user.set_password(password)
        #saves the user
        user.save(using=self._db)

        #returns the user
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

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