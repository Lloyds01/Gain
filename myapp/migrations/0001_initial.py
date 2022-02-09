# Generated by Django 3.2.4 on 2022-02-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
                ('event_hall', models.CharField(max_length=30)),
                ('hall_address', models.CharField(max_length=50)),
            ],
        ),
    ]
