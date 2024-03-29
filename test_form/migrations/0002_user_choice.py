# Generated by Django 2.2.6 on 2019-10-11 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField()),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_form.Choice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
