# Generated by Django 4.0.4 on 2022-04-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0005_remove_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('CHOOSE', 'Choose'), ('JAVA', 'Java'), ('JAVASCRIPT', 'Javascript'), ('PYTHON', 'Python'), ('.NET', '.Net')], default='', max_length=200, null=True),
        ),
    ]