# Generated by Django 3.0.3 on 2020-09-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCrime', '0004_auto_20200831_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='Status',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='missing_complaint',
            name='Status',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
