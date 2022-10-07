from django.forms import ModelForm
from .models import Issue
from accounts.models import Account


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'summary', 'description', 'status', 'assignee']
      
    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['assignee'].queryset = Account.objects.exclude(role='CUSTOMER')