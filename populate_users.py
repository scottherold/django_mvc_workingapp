"""
These scripts populate the AppTwo database with dummy data using the Faker
Library
"""

# NOTE: importing the Django settings must be done before anything else!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

# NOTE: Sets up the django environment from the above setup settings
import django
django.setup()

## FAKE POPULATION SCRIPT
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    """
    Function to populate database with fake data using the Faker library. The
    user can input the amount of fake data being populated, with the function
    defaulting to 5 iterations.

    For each iteration, the function generates fake data using the Faker
    library, and creates a new User entry in the linked database table using
    the get_or_create() method. This method queries the database for the data
    provided in the method's parameters, and if the data is present, it is
    qeuried; if the data is not present, it is inserted as a new entry. The
    data is then returned as a single item tuple.
    """
    for entry in range(N):
        # Create the fake data for the entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create the new User entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    """invokes the populate() function with 20 iterations"""
    print('Populating the data!')
    populate(20)
    print('Populating complete!')