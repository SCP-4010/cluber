# Generated by Django 3.0.8 on 2020-07-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluberapp', '0004_music_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='icon',
            field=models.ImageField(default='', upload_to='icons/'),
        ),
    ]
