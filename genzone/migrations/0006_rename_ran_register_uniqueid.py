# Generated by Django 4.2.1 on 2023-05-10 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genzone', '0005_register_ran'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='ran',
            new_name='uniqueID',
        ),
    ]
