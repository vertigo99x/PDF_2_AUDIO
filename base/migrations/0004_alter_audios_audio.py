# Generated by Django 4.1.6 on 2023-06-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_audios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audios',
            name='audio',
            field=models.FileField(upload_to='audios/'),
        ),
    ]