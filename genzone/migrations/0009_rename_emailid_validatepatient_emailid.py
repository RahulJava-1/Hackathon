# Generated by Django 4.2.1 on 2023-05-10 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genzone', '0008_rename_email_validatepatient_emailid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='validatepatient',
            old_name='emailID',
            new_name='emailid',
        ),
    ]