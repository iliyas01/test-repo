# Generated by Django 3.0.6 on 2022-03-31 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('JAVA', 'Java'), ('JAVASCRIPT', 'Javascript'), ('PYTHON', 'Python'), ('.NET', '.Net')], default='', max_length=200, null=True),
        ),
    ]
