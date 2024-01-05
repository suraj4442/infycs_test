# Generated by Django 5.0 on 2024-01-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('resume', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('summary', models.TextField(default=None)),
            ],
        ),
    ]
