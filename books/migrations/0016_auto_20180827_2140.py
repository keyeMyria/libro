# Generated by Django 2.0.1 on 2018-08-27 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20180827_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_liked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_liked', to='books.BookLike'),
        ),
    ]
