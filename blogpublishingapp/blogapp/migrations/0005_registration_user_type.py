# Generated by Django 4.1.7 on 2023-03-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='user_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
