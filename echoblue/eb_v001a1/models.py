import uuid
from django.db import models
from decimal import Decimal

# Organization models


class Organization(models.Model):
    YES = '1'
    NO = '0'

    ORG_ISCHILD_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    ORG_ISTESTDATA_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    istestdata = models.CharField(max_length=1, default=YES)
    org_id = models.CharField(max_length=8, unique=True)
    org_fullname = models.CharField(max_length=100)
    org_shortname = models.CharField(max_length=25)
    org_ischild = models.CharField(max_length=1, choices=ORG_ISCHILD_CHOICES, default=NO)

    def __unicode__(self):
        return self.org_id


class Organization_children(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    org_id = models.ForeignKey('Organization', to_field='org_id')
    org_parent = models.ForeignKey('Organization', to_field='org_parent')

    def __unicode__(self):
        return self.org_id


class Organization_location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    org_id = models.ForeignKey('Organization', to_field='org_id')
    org_country = models.CharField(max_length=100)
    org_region = models.CharField(max_length=100)
    org_city = models.CharField(max_length=100)
    org_postcode = models.CharField(max_length=16)
    org_street = models.CharField(max_length=50)
    org_streetnumber = models.IntegerField()
    org_boxnumber = models.CharField(max_length=4)

    def __unicode__(self):
        return self.org_id


class Organization_description(models.Model):
    #TODO: Enrollment figures should be pre-calc'd and added here
    UNDERGRADUATE = '1'
    GRADUATE = '2'
    MIXED = '3'
    RESIDENTIAL = '1'
    COMMUTER = '2'
    ONLINE = '3'
    PUBLIC = '1'
    PRIVATE = '2'
    NONPROFIT = '1'
    FORPROFIT = '2'

    ORG_TYPE_CHOICES = (
        (UNDERGRADUATE, 'Undergraduate'),
        (GRADUATE, 'Graduate'),
        (MIXED, 'Mixed')
    )

    ORG_RES_TYPE_CHOICES = (
        (RESIDENTIAL, 'Residential'),
        (COMMUTER, 'Commuter'),
        (ONLINE, 'Online')
    )

    ORG_PUBLIC_TYPE_CHOICES = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private')

    )

    ORG_PROFIT_TYPE_CHOICES = (
        (NONPROFIT, 'Nonprofit'),
        (FORPROFIT, 'For profit')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    org_id = models.ForeignKey('Organization', to_field='org_id')
    org_type = models.CharField(max_length=1, choices=ORG_TYPE_CHOICES)
    org_res_type = models.CharField(max_length=1, choices=ORG_RES_TYPE_CHOICES)
    org_public_type = models.CharField(max_length=1, choices=ORG_PUBLIC_TYPE_CHOICES)
    org_profit_type = models.CharField(max_length=1, choices=ORG_PROFIT_TYPE_CHOICES)

    def __unicode__(self):
        return self.org_id

#Student models


class Student(models.Model):
    YES = '1'
    NO = '0'

    STUDENT_ISTESTDATA_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    istestdata = models.CharField(max_length=1, choices=STUDENT_ISTESTDATA_CHOICES, default=YES)
    student_id = models.CharField(max_length=16, unique=True)
    student_name_first = models.CharField(max_length=64)
    student_name_last = models.CharField(max_length=64)
    student_name_middle = models.CharField(max_length=64)
    student_name_suffix = models.CharField(max_length=4)
    student_dob = models.DateField()

    def __unicode__(self):
        return self.student_id


class Student_demogdata(models.Model):
    YES = '1'
    NO = '0'
    FEMALE = '1'
    MALE = '2'
    TRANS = '3'
    CIS = '4'
    WHITE = '1'
    BLACK = '2'
    AMIND = '3'
    ASIAN = '4'
    PACISL = '5'
    DND = '6'

    STUDENT_GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (TRANS, 'Trans'),
        (CIS, 'Cis')
    )

    STUDENT_RACE_CHOICES = (
        (DND, 'Not specified'),
        (WHITE, 'White'),
        (BLACK, 'Black or African American'),
        (AMIND, 'American Indian and Alaskan Native'),
        (ASIAN, 'Asian'),
        (PACISL, 'Native Hawaiian and Other Pacific Islander')
    )

    STUDENT_HISPANIC_CHOICES = (
        (YES, 'Hispanic/Latino/Spanish'),
        (NO, 'Not Hispanic/Latino/Spanish')
    )


    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id')
    student_gender = models.CharField(max_length=1, choices=STUDENT_GENDER_CHOICES)
    student_race = models.CharField(max_length=1, choices=STUDENT_RACE_CHOICES, default=DND)
    student_hispanic = models.CharField(max_length=1, choices=STUDENT_HISPANIC_CHOICES, default=NO)


#ODD = Organization defined data
class Student_odd(models.Model):
    UNDERGRADUATE = '1'
    GRADUATE = '2'
    UNENROLLED = '3'
    GRADUATED = '4'
    ELIGIBLE = '1'
    INELIGIBLE = '2'
    FRESHMAN = '1'
    SOPHOMORE = '2'
    JUNIOR = '3'
    SENIOR = '4'

    STUDENT_ODD_ENROLLSTATUS_CHOICES = (
        (UNDERGRADUATE, 'Undergraduate'),
        (GRADUATE, 'Graduate'),
        (UNENROLLED, 'Unenrolled'),
        (GRADUATED, 'Graduated')
    )

    STUDENT_ODD_HOUSINGELIG_CHOICES = (
        (ELIGIBLE, 'Eligible'),
        (INELIGIBLE, 'Ineligible')
    )

    STUDENT_ODD_UNDERGRADLEVEL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id')
    #Native ID number used at the organization
    student_odd_id = models.CharField(max_length=25)
    student_odd_networkid = models.CharField(max_length=25)
    student_odd_enrollstatus = models.CharField(max_length=1, choices=STUDENT_ODD_ENROLLSTATUS_CHOICES)
    student_odd_housingelig = models.CharField(max_length=1, choices=STUDENT_ODD_HOUSINGELIG_CHOICES)
    student_odd_undergradlevel = models.CharField(max_length=1, choices=STUDENT_ODD_UNDERGRADLEVEL_CHOICES)
    #TODO: Filter and precalc ODD so that queries hit this table and can batch load academic data
    student_odd_major = models.CharField(max_length=50)
    student_odd_major2 = models.CharField(max_length=50)
    student_odd_minor = models.CharField(max_length=50)
    student_odd_minor2 = models.CharField(max_length=50)
    student_odd_credits = models.DecimalField(default=Decimal('0.00'), max_digits=5, decimal_places=2)
    student_odd_gpa = models.DecimalField(default=Decimal('0.0000'), max_digits=5, decimal_places=4)

    def __unicode__(self):
        return self.student_id


class Student_contact_oncampus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id')
    student_phone_main_countrycode = models.CharField(max_length=2)
    student_phone_main_digits = models.CharField(max_length=16)
    student_phone_main_ext = models.CharField(max_length=8)
    student_phone_2_countrycode = models.CharField(max_length=2)
    student_phone_2_digits = models.CharField(max_length=16)
    student_phone_2_ext = models.CharField(max_length=8)
    #TODO: Link oncampus data to housing module

    def __unicode__(self):
        return self.student_id

    
class Student_contact_offcampus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id')
    student_offcampus_country = models.CharField(max_length=100)
    student_offcampus_region = models.CharField(max_length=100)
    student_offcampus_city = models.CharField(max_length=100)
    student_offcampus_postcode = models.CharField(max_length=16)
    student_offcampus_street = models.CharField(max_length=50)
    student_offcampus_streetnumber = models.IntegerField()
    student_offcampus_boxnumber = models.CharField(max_length=4)

    def __unicode__(self):
        return self.student_id