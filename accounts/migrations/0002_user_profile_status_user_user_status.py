# Generated by Django 4.1.5 on 2023-03-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_status',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Deleted')], null=True),
        ),
    ]
