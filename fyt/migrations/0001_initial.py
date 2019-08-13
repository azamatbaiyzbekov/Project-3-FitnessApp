# Generated by Django 2.2.4 on 2019-08-12 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=50, verbose_name='Workout ')),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name_1', models.CharField(max_length=50, verbose_name='Exercise ')),
                ('sets_1', models.PositiveIntegerField(default='0', verbose_name='Sets ')),
                ('reps_1', models.PositiveIntegerField(default='0', verbose_name='Reps')),
                ('exercise_name_2', models.CharField(max_length=50, verbose_name='Exercise ')),
                ('sets_2', models.PositiveIntegerField(default='0', verbose_name='Sets ')),
                ('reps_2', models.PositiveIntegerField(default='0', verbose_name='Reps ')),
                ('exercise_name_3', models.CharField(max_length=50, verbose_name='Exercise ')),
                ('sets_3', models.PositiveIntegerField(default='0', verbose_name='Sets ')),
                ('reps_3', models.PositiveIntegerField(default='0', verbose_name='Reps ')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='fyt.Workout')),
            ],
        ),
    ]
