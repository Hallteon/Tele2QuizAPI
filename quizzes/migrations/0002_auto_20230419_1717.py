# Generated by Django 3.2.18 on 2023-04-19 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='Quiz',
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Квиз', 'verbose_name_plural': 'Квизы'},
        ),
    ]