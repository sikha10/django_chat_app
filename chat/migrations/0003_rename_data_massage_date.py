# Generated by Django 4.0.5 on 2022-09-04 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_massage_room_alter_massage_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='massage',
            old_name='data',
            new_name='date',
        ),
    ]
