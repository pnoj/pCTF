# Generated by Django 3.1.4 on 2020-12-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameserver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='summary',
            field=models.CharField(default='sdf', max_length=150),
            preserve_default=False,
        ),
    ]