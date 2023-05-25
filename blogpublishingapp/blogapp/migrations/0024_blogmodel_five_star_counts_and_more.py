# Generated by Django 4.1.7 on 2023-05-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0023_blogmodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='five_star_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='four_star_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='one_star_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='three_star_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='two_star_counts',
            field=models.IntegerField(default=0),
        ),
    ]