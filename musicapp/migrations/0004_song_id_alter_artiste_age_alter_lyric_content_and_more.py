# Generated by Django 4.1.2 on 2022-10-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_rename_song_id_lyric_song_alter_lyric_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artiste',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='song',
            name='artiste_id',
            field=models.IntegerField(),
        ),
    ]