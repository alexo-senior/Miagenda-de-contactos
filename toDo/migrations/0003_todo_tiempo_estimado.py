# Generated by Django 5.1.4 on 2025-01-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toDo", "0002_rename_task_todo"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="tiempo_estimado",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
