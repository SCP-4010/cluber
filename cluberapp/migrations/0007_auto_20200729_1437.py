# Generated by Django 3.0.8 on 2020-07-29 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cluberapp', '0006_auto_20200729_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(default='Single', on_delete=django.db.models.deletion.CASCADE, to='cluberapp.Album'),
        ),
    ]
