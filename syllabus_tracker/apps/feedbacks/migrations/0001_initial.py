# Generated by Django 4.2 on 2025-01-19 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('comments', models.TextField(blank=True, help_text='Optional comments by the student', null=True)),
                ('feedback_date', models.DateField(auto_now_add=True, help_text='The date the feedback was given')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='lectures.lecture')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='accounts.student')),
            ],
            options={
                'unique_together': {('lecture', 'student')},
            },
        ),
    ]
