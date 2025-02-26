# Generated by Django 5.1.4 on 2025-01-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toDo", "0005_todo_tiempo_estimado"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="fecha_finalizacion",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="todo",
            name="prioridad",
            field=models.CharField(
                choices=[("B", "baja"), ("M", "media"), ("A", "alta")],
                default="B",
                max_length=1,
            ),
        ),
    ]
