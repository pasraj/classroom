# Generated by Django 3.2.9 on 2021-11-24 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0006_alter_subject_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.teacher'),
        ),
    ]
