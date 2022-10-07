from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Issue, Status
from .forms import IssueForm


class IssueContextListView(LoginRequiredMixin, ListView):
    template_name: str='issues/list_status.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_status = Status.objects.get(name=kwargs["status_name"])
        context['issue_list'] = Issue.objects.filter(
                                requester=self.request.user).filter(
                                    status=issue_status).order_by(
                                        "created_on")
        return context

class IssueListView(LoginRequiredMixin, ListView):
    template_name: str='issues/list.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue_list'] = Issue.objects.filter(
                                requester=self.request.user).order_by(
                                        "created_on")
        return context

class IssueToDoListView(IssueContextListView):
    status = "To Do"

    def get_context_data(self):
        return super().get_context_data(status_name=self.status)

class IssueInProgressListView(IssueContextListView):
    status = "In Progress"

    def get_context_data(self):
        return super().get_context_data(status_name=self.status)

class IssueDoneListView(IssueContextListView):
    status = "Done"

    def get_context_data(self):
        return super().get_context_data(status_name=self.status)

class IssueDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name: str='issues/detail.html'
    model = Issue

    def test_func(self):
        issue_obj = self.get_object()
        return issue_obj.requester == self.request.user

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name: str='issues/new.html'
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name: str='issues/update.html'
    model = Issue
    form_class = IssueForm

    def test_func(self):
        issue_obj = self.get_object()
        return issue_obj.requester == self.request.user

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name: str='issues/delete.html'
    model = Issue
    success_url: reverse_lazy('list')

    def test_func(self):
        issue_obj = self.get_object()
        return issue_obj.requester == self.request.user