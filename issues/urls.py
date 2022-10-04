from django.urls import path
from .views import (
    IssueListView,
    IssueToDoListView,
    IssueInProgressListView,
    IssueDoneListView,
    IssueDetailView,
    IssueUpdateView,
    IssueCreateView,
    IssueDeleteView
)

urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    path('todo/', IssueToDoListView.as_view(), name='todo_list'),
    path('in-progress/', IssueInProgressListView.as_view(), name='in_progress_list'),
    path('done/', IssueDoneListView.as_view(), name='done_list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', IssueUpdateView.as_view(), name='update'),
    path('new/', IssueCreateView.as_view(), name='new'),
    path('delete/<int:pk>/', IssueDeleteView.as_view(), name='delete'),
]