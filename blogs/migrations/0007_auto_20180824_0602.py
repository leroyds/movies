# Generated by Django 2.1 on 2018-08-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20180823_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ratings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('A', 'ACTIVE'), ('D', 'INACTIVE')], default='A', max_length=50),
        ),
    ]