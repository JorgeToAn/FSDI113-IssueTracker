# Generated by Django 4.1.1 on 2022-10-07 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_agent_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
