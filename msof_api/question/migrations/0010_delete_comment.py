# Generated by Django 3.1.7 on 2021-07-24 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_auto_20210712_0052'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]