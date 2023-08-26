# Generated by Django 4.1.2 on 2022-10-16 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_alter_semesterbill_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
                ('courseCode', models.IntegerField()),
                ('paperNo', models.IntegerField(default=0)),
                ('tPaperNo', models.IntegerField(default=0)),
                ('external', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external', to='root.faculty')),
                ('internal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internal', to='root.faculty')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.session')),
                ('thirdExaminer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thirdExaminer', to='root.faculty')),
            ],
        ),
    ]
