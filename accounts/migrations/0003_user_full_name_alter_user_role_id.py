# Generated by Django 4.1.5 on 2023-03-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profile_status_user_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Student'), (3, 'Mentor')], default=1, null=True),
        ),
    ]