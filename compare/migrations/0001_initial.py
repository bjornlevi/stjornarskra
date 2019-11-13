# Generated by Django 2.2.6 on 2019-10-23 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('origin', models.IntegerField(choices=[(1, 'Stjórnarskrá'), (2, 'Frumvarp')], default=1)),
                ('article_nr', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.IntegerField()),
                ('frumvarp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frumvarp', to='compare.Sentence')),
                ('stjornarskra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stjornarskra', to='compare.Sentence')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr', models.CharField(max_length=3, unique=True)),
                ('sentences', models.ManyToManyField(to='compare.Sentence')),
            ],
        ),
    ]
