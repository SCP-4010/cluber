# Generated by Django 3.0.8 on 2020-07-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluberapp', '0003_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.CharField(default='', max_length=120),
        ),
    ]