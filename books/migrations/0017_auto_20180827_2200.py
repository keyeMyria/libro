# Generated by Django 2.0.1 on 2018-08-27 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20180827_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_liked',
            new_name='like',
        ),
    ]
