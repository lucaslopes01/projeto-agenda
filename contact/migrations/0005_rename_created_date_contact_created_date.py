# Generated by Django 5.0.3 on 2024-05-16 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_Date',
            new_name='created_date',
        ),
    ]
