# Generated by Django 4.2.2 on 2023-06-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('no_of_line', models.IntegerField()),
            ],
        ),
    ]
