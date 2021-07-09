# Generated by Django 3.2.4 on 2021-07-08 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0075_auto_20210709_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 18, 30, 28, 314186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 18, 30, 28, 314186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 18, 30, 28, 314186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 18, 30, 28, 314186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 18, 30, 28, 314186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 18, 30, 28, 314186, tzinfo=utc)),
        ),
        migrations.AddConstraint(
            model_name='blocksection',
            constraint=models.UniqueConstraint(fields=('blockYear', 'blockSection', 'blockCourse'), name='block section'),
        ),
        migrations.AddConstraint(
            model_name='curriculuminfo',
            constraint=models.UniqueConstraint(fields=('curriculumyear', 'schoolYear', 'schoolSem', 'departmentID', 'subjectCode'), name='curriculum'),
        ),
        migrations.AddConstraint(
            model_name='department',
            constraint=models.UniqueConstraint(fields=('collegeId', 'courseName'), name='Department'),
        ),
        migrations.AddConstraint(
            model_name='subjectinfo',
            constraint=models.UniqueConstraint(fields=('subjectCode', 'subjectName', 'college'), name='subject'),
        ),
    ]
