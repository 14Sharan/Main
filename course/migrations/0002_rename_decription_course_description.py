# Generated by Django 4.1.5 on 2023-04-22 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='decription',
            new_name='description',
        ),
    ]
