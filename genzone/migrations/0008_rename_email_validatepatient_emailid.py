# Generated by Django 4.2.1 on 2023-05-10 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genzone', '0007_rename_validateuser_validatepatient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='validatepatient',
            old_name='email',
            new_name='emailID',
        ),
    ]
