# Generated by Django 4.1.7 on 2023-05-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0020_alter_registration_profile_pic_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default-avatar.bacg1.png', null=True, upload_to='profile'),
        ),
    ]
