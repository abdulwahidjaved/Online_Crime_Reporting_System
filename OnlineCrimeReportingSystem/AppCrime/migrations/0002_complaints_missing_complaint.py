# Generated by Django 3.0.3 on 2020-08-31 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCrime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.CharField(max_length=50)),
                ('FullName', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('Email', models.CharField(default=None, max_length=50)),
                ('Address', models.CharField(max_length=10)),
                ('City', models.IntegerField(default=None)),
                ('State', models.EmailField(max_length=254)),
                ('Country', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=100)),
                ('Complaint', models.CharField(max_length=100)),
                ('ComplaintType', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Complaints',
            },
        ),
        migrations.CreateModel(
            name='Missing_Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.CharField(max_length=50)),
                ('FullName', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('Email', models.CharField(default=None, max_length=50)),
                ('Address', models.CharField(max_length=10)),
                ('City', models.IntegerField(default=None)),
                ('State', models.EmailField(max_length=254)),
                ('Country', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=100)),
                ('MissingDetails', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='img/images/ComplaintImages')),
            ],
            options={
                'db_table': 'Missing_Complaint',
            },
        ),
    ]
