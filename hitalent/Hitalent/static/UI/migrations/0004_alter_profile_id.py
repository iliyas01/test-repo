# Generated by Django 4.0.3 on 2022-03-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0003_merge_20220326_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
