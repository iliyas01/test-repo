# Generated by Django 3.0.6 on 2022-03-29 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='', max_length=200, null=True)),
                ('avatar', models.ImageField(default='avatar.svg', upload_to='avatars')),
                ('bio', models.TextField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('educational_details', models.TextField(null=True)),
                ('git_profile', models.CharField(max_length=200, null=True, unique=True)),
                ('phone', models.IntegerField(null=True, unique=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]