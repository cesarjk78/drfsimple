# Generated by Django 5.1.2 on 2024-10-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_nickname_programmer_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmer',
            name='apodo',
            field=models.CharField(default='Sin Apodo', max_length=60),
        ),
    ]