# Generated by Django 4.0 on 2021-12-26 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_content',
            new_name='content',
        ),
    ]
