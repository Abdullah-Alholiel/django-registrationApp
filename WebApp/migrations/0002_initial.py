# Generated by Django 4.2.3 on 2023-07-13 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='module',
            name='groups',
            field=models.ManyToManyField(related_name='modules', to='auth.group'),
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('student', 'module')},
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together={('name', 'code')},
        ),
    ]
