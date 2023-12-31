# Generated by Django 4.2.7 on 2023-11-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('ClassID', models.AutoField(primary_key=True, serialize=False)),
                ('Subject', models.CharField(max_length=255)),
                ('HoursPerWeek', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassID', models.IntegerField()),
                ('ClassLetter', models.CharField(max_length=1)),
                ('Subject', models.CharField(max_length=255)),
                ('TeacherID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('TeacherID', models.AutoField(primary_key=True, serialize=False)),
                ('TeacherName', models.CharField(max_length=255)),
                ('Specialization', models.CharField(max_length=255)),
                ('Experience', models.IntegerField()),
            ],
        ),
    ]
