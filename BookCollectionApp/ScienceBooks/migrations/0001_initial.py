# Generated by Django 3.0.2 on 2020-01-24 01:24

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(blank=True, max_length=200)),
                ('publication_date', models.CharField(blank=True, default=None, max_length=50)),
                ('google_reviews', models.CharField(blank=True, default=None, max_length=3)),
            ],
            managers=[
                ('Books', django.db.models.manager.Manager()),
            ],
        ),
    ]
