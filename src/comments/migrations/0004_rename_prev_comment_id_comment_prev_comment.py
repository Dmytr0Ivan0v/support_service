# Generated by Django 4.1.5 on 2023-02-02 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0003_comment_prev_comment_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="prev_comment_id",
            new_name="prev_comment",
        ),
    ]