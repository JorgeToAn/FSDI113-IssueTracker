from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models import Q

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Issue(models.Model):
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=256)
    description = models.TextField()
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    requester = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='requester'
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='assignee',
        blank=True,
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])