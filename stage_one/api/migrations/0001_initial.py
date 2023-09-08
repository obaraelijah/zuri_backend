# Generated by Django 4.0.6 on 2023-09-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(max_length=100)),
                ('utc_now', models.DateTimeField()),
                ('track', models.CharField(max_length=100)),
                ('github_file_url', models.URLField()),
                ('github_repo_url', models.URLField()),
            ],
        ),
    ]
