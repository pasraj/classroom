# Generated by Django 3.2.9 on 2021-11-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0008_subject_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='status',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
