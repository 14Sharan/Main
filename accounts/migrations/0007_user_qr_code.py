# Generated by Django 4.1.5 on 2023-04-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='qr_code',
            field=models.TextField(blank=True, null=True),
        ),
    ]
