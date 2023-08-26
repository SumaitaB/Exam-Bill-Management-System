# Generated by Django 4.1.2 on 2022-10-15 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='External',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semId', models.IntegerField()),
                ('chairman', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chairman', to='root.faculty')),
                ('external', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.external')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moderator', models.IntegerField(default=0)),
                ('translator', models.IntegerField(default=0)),
                ('typist', models.IntegerField(default=0)),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='root.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.session')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='root.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='semester',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.session'),
        ),
        migrations.AddField(
            model_name='semester',
            name='tabular1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabular1', to='root.faculty'),
        ),
        migrations.AddField(
            model_name='semester',
            name='tabular2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabular2', to='root.faculty'),
        ),
    ]
