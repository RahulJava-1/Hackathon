# Generated by Django 4.2 on 2023-05-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzone', '0012_adminlogin_delete_validatedoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorLogin',
            fields=[
                ('docid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
