# Generated by Django 5.0.6 on 2024-07-16 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_edit_post', 'Can edit post')]},
        ),
    ]
