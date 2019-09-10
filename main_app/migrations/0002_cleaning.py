# Generated by Django 2.2.5 on 2019-09-10 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='feeding date')),
                ('cleaning', models.CharField(choices=[('H', 'Hull'), ('D', 'Deck'), ('I', 'Interior')], default='H', max_length=1)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Boat')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
