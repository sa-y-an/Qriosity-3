# Generated by Django 3.0.7 on 2020-07-20 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20200720_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_submit',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 19, 54, 6, 731254)),
        ),
        migrations.CreateModel(
            name='StageOneHint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(blank=True, default=0)),
                ('taken', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Player')),
            ],
        ),
    ]