# Generated by Django 4.2 on 2023-05-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminzone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adddoc',
            name='id',
        ),
        migrations.AlterField(
            model_name='adddoc',
            name='docId',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
