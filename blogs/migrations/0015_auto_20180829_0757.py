# Generated by Django 2.1 on 2018-08-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_auto_20180829_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'INACTIVE'), ('A', 'ACTIVE')], default='A', max_length=50),
        ),
    ]
