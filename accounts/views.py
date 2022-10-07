from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AccountCreationForm
from .models import Account


class SignUpView(CreateView):
    template_name: str='registration/signup.html'
    form_class = AccountCreationForm
    model = Account
    success_url = reverse_lazy('login')