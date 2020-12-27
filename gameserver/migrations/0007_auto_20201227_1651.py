# Generated by Django 3.1.4 on 2020-12-27 16:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameserver', '0006_auto_20201227_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='access_code',
        ),
        migrations.RemoveField(
            model_name='contest',
            name='is_public',
        ),
        migrations.AddField(
            model_name='contest',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
    ]
