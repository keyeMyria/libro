# Generated by Django 2.0.1 on 2018-08-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
