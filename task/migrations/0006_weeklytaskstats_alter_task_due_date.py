# Generated by Django 4.2.6 on 2023-10-27 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyTaskStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField()),
                ('total_assigned_tasks', models.IntegerField()),
                ('total_completed_tasks', models.IntegerField()),
                ('total_pending_tasks', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 3, 7, 50, 25, 936088, tzinfo=datetime.timezone.utc)),
        ),
    ]
