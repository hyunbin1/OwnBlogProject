# Generated by Django 3.1 on 2020-08-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('content', models.TextField(null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
