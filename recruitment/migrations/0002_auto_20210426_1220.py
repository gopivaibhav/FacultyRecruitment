# Generated by Django 2.2.20 on 2021-04-26 06:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educational_qualifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=10)),
                ('subjects', models.CharField(max_length=200)),
                ('year_of_passing', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employment_exp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=250)),
                ('from_year', models.IntegerField()),
                ('to_year', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('nature', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime(2021, 4, 26, 6, 50, 46, 365852, tzinfo=utc))),
                ('father_name', models.CharField(max_length=200)),
                ('address_perm', models.CharField(max_length=200)),
                ('telephone_perm', models.CharField(max_length=20)),
                ('address_mail', models.CharField(max_length=200)),
                ('telephone_mail', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Not Married', 'Not Married')], max_length=10)),
                ('nationality', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('General', 'General'), ('OBC-CL', 'OBC-CL'), ('OBC-NCL', 'OBC-NCL'), ('ST', 'ST'), ('SC', 'SC'), ('Gen-PwD', 'Gen-PwD'), ('OBC-CL-PwD', 'OBC-CL-PwD'), ('OBC-NCL-PwD', 'OBC-NCL-PwD'), ('ST-PwD', 'ST-Pwd'), ('SC-PwD', 'SC-PwD')], max_length=10)),
                ('reservation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('present_employer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='other_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.TextField()),
                ('responsibilities', models.TextField()),
                ('academic_year_break', models.TextField()),
                ('college_punishment', models.TextField()),
                ('judicial_punishment', models.TextField()),
                ('unfit_for_position', models.TextField()),
                ('references', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PhD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhD_awarded', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('title_of_thesis', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='professional_detail',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='teaching_and_research_detail',
            name='applicant',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 26, 6, 50, 46, 360291, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Other_important_details',
        ),
        migrations.DeleteModel(
            name='Professional_detail',
        ),
        migrations.DeleteModel(
            name='Teaching_and_research_detail',
        ),
        migrations.AddField(
            model_name='phd',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PhD', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='other_info',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_info', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='general',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='General', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='employment_exp',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employment_exp', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='educational_qualifications',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Educational_qualifications', to='recruitment.Applicant'),
        ),
    ]
