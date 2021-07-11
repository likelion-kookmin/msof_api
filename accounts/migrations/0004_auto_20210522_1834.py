# Generated by Django 3.1.7 on 2021-05-22 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210417_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='univerisity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.univerisity', verbose_name='대학'),
        ),
    ]