# Generated by Django 3.1.7 on 2021-03-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perform', '0002_auto_20210321_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perform',
            name='category',
            field=models.IntegerField(choices=[(0, 'none'), (1, 'like'), (2, 'dislike')], default=0, verbose_name='종류'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='삭제된 일시'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정된 일시'),
        ),
    ]
