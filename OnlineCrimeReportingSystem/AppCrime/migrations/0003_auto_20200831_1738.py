# Generated by Django 3.0.3 on 2020-08-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCrime', '0002_complaints_missing_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='Uid',
            new_name='Userid',
        ),
        migrations.AlterField(
            model_name='complaints',
            name='Address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='FullName',
            field=models.CharField(max_length=100),
        ),
    ]
