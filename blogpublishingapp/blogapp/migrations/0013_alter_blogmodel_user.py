# Generated by Django 4.1.7 on 2023-04-23 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0012_remove_registration_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
