# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('istestdata', models.CharField(default=b'1', max_length=1)),
                ('org_id', models.CharField(unique=True, max_length=8)),
                ('org_fullname', models.CharField(max_length=100)),
                ('org_shortname', models.CharField(max_length=25)),
                ('org_ischild', models.CharField(default=b'0', max_length=1, choices=[(b'1', b'Yes'), (b'0', b'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Organization_children',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('org_id', models.ForeignKey(related_name='+', to='eb_v001a1.Organization', to_field=b'org_id')),
                ('org_parent', models.ForeignKey(related_query_name=b'Parent organization ID', to='eb_v001a1.Organization', to_field=b'org_id')),
            ],
        ),
        migrations.CreateModel(
            name='Organization_description',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('org_type', models.CharField(max_length=1, choices=[(b'1', b'Undergraduate'), (b'2', b'Graduate'), (b'3', b'Mixed')])),
                ('org_res_type', models.CharField(max_length=1, choices=[(b'1', b'Residential'), (b'2', b'Commuter'), (b'3', b'Online')])),
                ('org_public_type', models.CharField(max_length=1, choices=[(b'1', b'Public'), (b'2', b'Private')])),
                ('org_profit_type', models.CharField(max_length=1, choices=[(b'1', b'Nonprofit'), (b'2', b'For profit')])),
                ('org_id', models.ForeignKey(to='eb_v001a1.Organization', to_field=b'org_id')),
            ],
        ),
        migrations.CreateModel(
            name='Organization_location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('org_country', models.CharField(max_length=100)),
                ('org_region', models.CharField(max_length=100)),
                ('org_city', models.CharField(max_length=100)),
                ('org_postcode', models.CharField(max_length=16)),
                ('org_street', models.CharField(max_length=50)),
                ('org_streetnumber', models.IntegerField()),
                ('org_boxnumber', models.CharField(max_length=4)),
                ('org_id', models.ForeignKey(to='eb_v001a1.Organization', to_field=b'org_id')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('istestdata', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Yes'), (b'0', b'No')])),
                ('student_id', models.CharField(unique=True, max_length=16)),
                ('student_name_first', models.CharField(max_length=64)),
                ('student_name_last', models.CharField(max_length=64)),
                ('student_name_middle', models.CharField(max_length=64)),
                ('student_name_suffix', models.CharField(max_length=4)),
                ('student_dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_contact_offcampus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('student_offcampus_country', models.CharField(max_length=100)),
                ('student_offcampus_region', models.CharField(max_length=100)),
                ('student_offcampus_city', models.CharField(max_length=100)),
                ('student_offcampus_postcode', models.CharField(max_length=16)),
                ('student_offcampus_street', models.CharField(max_length=50)),
                ('student_offcampus_streetnumber', models.IntegerField()),
                ('student_offcampus_boxnumber', models.CharField(max_length=4)),
                ('student_id', models.ForeignKey(to='eb_v001a1.Student', to_field=b'student_id')),
            ],
        ),
        migrations.CreateModel(
            name='Student_contact_oncampus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('student_phone_main_countrycode', models.CharField(max_length=2)),
                ('student_phone_main_digits', models.CharField(max_length=16)),
                ('student_phone_main_ext', models.CharField(max_length=8)),
                ('student_phone_2_countrycode', models.CharField(max_length=2)),
                ('student_phone_2_digits', models.CharField(max_length=16)),
                ('student_phone_2_ext', models.CharField(max_length=8)),
                ('student_id', models.ForeignKey(to='eb_v001a1.Student', to_field=b'student_id')),
            ],
        ),
        migrations.CreateModel(
            name='Student_demogdata',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('student_gender', models.CharField(max_length=1, choices=[(b'1', b'Female'), (b'2', b'Male'), (b'3', b'Trans'), (b'4', b'Cis')])),
                ('student_race', models.CharField(default=b'6', max_length=1, choices=[(b'6', b'Not specified'), (b'1', b'White'), (b'2', b'Black or African American'), (b'3', b'American Indian and Alaskan Native'), (b'4', b'Asian'), (b'5', b'Native Hawaiian and Other Pacific Islander')])),
                ('student_hispanic', models.CharField(default=b'0', max_length=1, choices=[(b'1', b'Hispanic/Latino/Spanish'), (b'0', b'Not Hispanic/Latino/Spanish')])),
                ('student_id', models.ForeignKey(to='eb_v001a1.Student', to_field=b'student_id')),
            ],
        ),
        migrations.CreateModel(
            name='Student_odd',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_edited', models.DateTimeField(auto_now=True)),
                ('student_odd_id', models.CharField(max_length=25)),
                ('student_odd_networkid', models.CharField(max_length=25)),
                ('student_odd_enrollstatus', models.CharField(max_length=1, choices=[(b'1', b'Undergraduate'), (b'2', b'Graduate'), (b'3', b'Unenrolled'), (b'4', b'Graduated')])),
                ('student_odd_housingelig', models.CharField(max_length=1, choices=[(b'1', b'Eligible'), (b'2', b'Ineligible')])),
                ('student_odd_undergradlevel', models.CharField(max_length=1, choices=[(b'1', b'Freshman'), (b'2', b'Sophomore'), (b'3', b'Junior'), (b'4', b'Senior')])),
                ('student_odd_major', models.CharField(max_length=50)),
                ('student_odd_major2', models.CharField(max_length=50)),
                ('student_odd_minor', models.CharField(max_length=50)),
                ('student_odd_minor2', models.CharField(max_length=50)),
                ('student_odd_credits', models.DecimalField(default=Decimal('0.00'), max_digits=5, decimal_places=2)),
                ('student_odd_gpa', models.DecimalField(default=Decimal('0.0000'), max_digits=5, decimal_places=4)),
                ('student_id', models.ForeignKey(to='eb_v001a1.Student', to_field=b'student_id')),
            ],
        ),
    ]
