# Generated by Django 5.0.7 on 2024-07-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
                ('label', models.CharField(choices=[('P', 'primary'), ('SE', 'secondary'), ('S', 'success'), ('DA', 'danger'), ('W', 'warning'), ('I', 'info'), ('L', 'light'), ('D', 'dark')], max_length=2)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
