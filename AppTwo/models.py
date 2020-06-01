from django.db import models

# Create your models here.
class User(models.Model):
    """
    User database model.

    Attributes:
        first_name (str): The user's first name, limited to 30 characters.
        last_name (str): The user's last name, limited to 30 characters.
        email (str): The user's email address, limited to 254 characters. The
        email address must be unique.

    Methods:
        __str__(): String representation of the class
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # EmailField is a CharField that validates email syntax
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email