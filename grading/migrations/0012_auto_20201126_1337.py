# Generated by Django 3.1.3 on 2020-11-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0011_auto_20201124_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='code',
            field=models.CharField(default='tny2eh', max_length=6),
        ),
    ]
