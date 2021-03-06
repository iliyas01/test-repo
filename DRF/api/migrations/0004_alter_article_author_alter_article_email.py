# Generated by Django 4.0.3 on 2022-03-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
