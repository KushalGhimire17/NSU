# Generated by Django 3.0.8 on 2020-08-13 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('mobile_number', models.IntegerField()),
                ('province', models.CharField(choices=[('1', 'Province No. 1'), ('2', 'Province No. 2'), ('3', 'Bagmati Pradesh'), ('4', 'Gandaki Pradesh'), ('5', 'Province No. 5'), ('6', 'Karnali Pradesh'), ('7', 'Sudurpashchim Pradesh')], max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('campus', models.CharField(max_length=200)),
                ('current_role', models.CharField(max_length=50)),
                ('municipality', models.CharField(max_length=100)),
                ('ward', models.IntegerField()),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
