# Generated by Django 4.2.3 on 2023-07-13 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_alter_registration_unique_together_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
