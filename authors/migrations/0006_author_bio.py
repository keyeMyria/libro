# Generated by Django 2.0.1 on 2018-08-23 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_auto_20180823_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]