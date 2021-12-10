# Generated by Django 4.0 on 2021-12-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0005_elfunit_armor_elfunit_weapons_orksunit_armor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Army',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('army_type', models.CharField(choices=[('Ork', 'Army of Orks'), ('Elf', 'Army of Elfs')], max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='elfunit',
            name='armor',
            field=models.ManyToManyField(blank=True, to='Roster.Armor'),
        ),
        migrations.AlterField(
            model_name='elfunit',
            name='weapons',
            field=models.ManyToManyField(blank=True, to='Roster.Weapon'),
        ),
        migrations.AlterField(
            model_name='orksunit',
            name='armor',
            field=models.ManyToManyField(blank=True, to='Roster.Armor'),
        ),
        migrations.AlterField(
            model_name='orksunit',
            name='weapons',
            field=models.ManyToManyField(blank=True, to='Roster.Weapon'),
        ),
    ]
