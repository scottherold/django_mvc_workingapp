from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import UserForm


# Create your views here.
def index(request):
    """Renders the AppTwp/index/html file."""
    return render(request, 'AppTwo/index.html')


def users(request):
    """
    Renders the users.html page from templates/AppTwo.

    Instantiates a form object.

    Queries the database for the User list, and produces a dictionary
    of User data.

    If the request received from the client is a POST method, the form object
    is passed the received data. If that data is valid, the data is saved to
    the database as a new user, the empty form is reinstantiated, and both the
    queried users and a blank form are passed to users.html as context.
    
    If the request is received via any other method, the initial form object is
    passed to users.html as context along with the queried user list.
    """
    # Create a form
    form = UserForm()

    # Query for Users
    user_list = User.objects.order_by('email')
    users_context = {'users': user_list, 'user_form': form}

    # Validators/Save to DB
    if request.method == 'POST':
        form = UserForm(request.POST)
        form.save()
        form = UserForm()
        return render(request, 'AppTwo/users.html', context=users_context)

    return render(request, 'AppTwo/users.html', context=users_context)