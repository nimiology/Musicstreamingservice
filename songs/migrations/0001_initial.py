# Generated by Django 4.0 on 2022-01-08 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import songs.ulitis


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField(blank=True, max_length=512, null=True)),
                ('cover', models.ImageField(upload_to=songs.ulitis.upload_cover_path)),
                ('createDTime', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.SlugField(blank=True, max_length=102, unique=True)),
                ('songFile', models.FileField(upload_to=songs.ulitis.upload_cover_path, validators=[songs.ulitis.Validator])),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='songs.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='auth.user')),
                ('feature', models.ManyToManyField(blank=True, related_name='featurings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField(blank=True, max_length=512, unique=True)),
                ('cover', models.ImageField(blank=True, default='Playlist/cover/DEFAULT.png', null=True, upload_to=songs.ulitis.upload_cover_path)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('lastEdit', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='auth.user')),
                ('tracks', models.ManyToManyField(blank=True, related_name='playlists', to='songs.Track')),
            ],
        ),
    ]