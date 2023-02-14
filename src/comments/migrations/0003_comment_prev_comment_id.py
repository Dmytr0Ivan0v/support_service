# Generated by Django 4.1.5 on 2023-02-02 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0002_alter_comment_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="prev_comment_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="next",
                to="comments.comment",
            ),
        ),
    ]
