# Generated by Django 2.0.1 on 2018-08-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20180823_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('form_name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('genre_name',),
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('period_name',),
            },
        ),
        migrations.AlterField(
            model_name='theme',
            name='theme_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='forms',
            field=models.ManyToManyField(blank=True, to='books.Form'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(blank=True, to='books.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='periods',
            field=models.ManyToManyField(blank=True, to='books.Period'),
        ),
    ]
