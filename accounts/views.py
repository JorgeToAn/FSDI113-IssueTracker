from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    template_name: str='registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
