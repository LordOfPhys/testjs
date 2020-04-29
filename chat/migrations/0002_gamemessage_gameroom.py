# Generated by Django 2.2 on 2020-04-29 09:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.SlugField(unique=True)),
                ('name', models.TextField()),
                ('user_one', models.ForeignKey(on_delete='default', related_name='user_one', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(on_delete='default', related_name='user_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_m_x', models.CharField(default='0', max_length=100)),
                ('u_m_y', models.CharField(default='0', max_length=100)),
                ('u_x', models.CharField(default='0', max_length=100)),
                ('u_y', models.CharField(default='0', max_length=100)),
                ('room', models.ForeignKey(on_delete='default', related_name='room', to='chat.GameRoom')),
                ('user', models.ForeignKey(on_delete='default', related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
