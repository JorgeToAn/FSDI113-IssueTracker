# Generated by Django 4.1.1 on 2022-10-06 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_agent_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'permissions': (('set_as_assignee', 'can set themselves as assignee'),)},
        ),
    ]