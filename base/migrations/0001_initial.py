# Generated by Django 5.0.6 on 2024-07-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_nickname', models.TextField()),
                ('author_full_name', models.TextField()),
                ('book_name', models.TextField()),
                ('skin', models.TextField()),
                ('print_place', models.TextField()),
                ('printer', models.TextField()),
                ('print_year', models.TextField()),
                ('press', models.TextField()),
            ],
        ),
    ]