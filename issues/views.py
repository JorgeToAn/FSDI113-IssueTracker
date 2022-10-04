from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Issue, Status


class IssueContextListView(ListView):
    template_name: str='issues/list.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_status = Status.objects.get(name=kwargs["status_name"])
        context['issue_list'] = Issue.objects.filter(
                                requester=self.request.user).filter(
                                    status=issue_status).order_by(
                                        "created_on")
        return context

class IssueListView(ListView):
    template_name: str='issues/list.html'
    model = Issue

class IssueToDoListView(IssueContextListView):
    def get_context_data(self):
        return super().get_context_data(status_name="To Do")

class IssueInProgressListView(IssueContextListView):
    def get_context_data(self):
        return super().get_context_data(status_name="In Progress")

class IssueDoneListView(IssueContextListView):
    def get_context_data(self):
        return super().get_context_data(status_name="Done")

class IssueDetailView(DetailView):
    template_name: str='issues/detail.html'
    model = Issue

class IssueCreateView(CreateView):
    template_name: str='issues/new.html'
    model = Issue
    fields = ['title', 'summary', 'description', 'assignee', 'status']

class IssueUpdateView(UpdateView):
    template_name: str='issues/update.html'
    model = Issue
    fields = ['title', 'summary', 'description', 'assignee', 'status']

class IssueDeleteView(DeleteView):
    template_name: str='issues/delete.html'
    model = Issue