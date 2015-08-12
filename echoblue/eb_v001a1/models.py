import uuid
from django.db import models
from django.contrib.auth.models import User
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
    istestdata = models.CharField(max_length=1, default=YES, null=True)
    org_id = models.CharField(max_length=8, unique=True, null=True)
    org_fullname = models.CharField(max_length=100, null=True)
    org_shortname = models.CharField(max_length=25, null=True)
    org_ischild = models.CharField(max_length=1, choices=ORG_ISCHILD_CHOICES, default=NO, null=True)

    def __unicode__(self):
        return '%s' % self.org_id


class Organization_children(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    org_id = models.ForeignKey('Organization', to_field='org_id', related_name='+', null=True)
    org_parent = models.ForeignKey('Organization', to_field='org_id', related_query_name='Parent organization ID', null=True)

    def __unicode__(self):
        return '%s' % self.org_id


class Organization_location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    org_id = models.ForeignKey('Organization', to_field='org_id', null=True)
    org_country = models.CharField(max_length=100, null=True)
    org_region = models.CharField(max_length=100, null=True)
    org_city = models.CharField(max_length=100, null=True)
    org_postcode = models.CharField(max_length=16, null=True)
    org_street = models.CharField(max_length=50, null=True)
    org_streetnumber = models.IntegerField(null=True)
    org_boxnumber = models.CharField(max_length=4, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.org_id


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
    org_id = models.ForeignKey('Organization', to_field='org_id', null=True)
    org_type = models.CharField(max_length=1, choices=ORG_TYPE_CHOICES, null=True)
    org_res_type = models.CharField(max_length=1, choices=ORG_RES_TYPE_CHOICES, null=True)
    org_public_type = models.CharField(max_length=1, choices=ORG_PUBLIC_TYPE_CHOICES, null=True)
    org_profit_type = models.CharField(max_length=1, choices=ORG_PROFIT_TYPE_CHOICES, null=True)

    def __unicode__(self):
        return '%s' % self.org_id

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
    istestdata = models.CharField(max_length=1, choices=STUDENT_ISTESTDATA_CHOICES, default=YES, null=True)
    student_id = models.CharField(max_length=16, unique=True, null=True)
    student_name_first = models.CharField(max_length=64, null=True)
    student_name_last = models.CharField(max_length=64, null=True)
    student_name_middle = models.CharField(max_length=64, null=True)
    student_name_suffix = models.CharField(max_length=4, null=True)
    student_dob = models.DateField()

    def __unicode__(self):
        return '%s' % self.student_id


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
    student_id = models.ForeignKey('Student', to_field='student_id', null=True)
    student_gender = models.CharField(max_length=1, choices=STUDENT_GENDER_CHOICES, null=True)
    student_race = models.CharField(max_length=1, choices=STUDENT_RACE_CHOICES, default=DND, null=True)
    student_hispanic = models.CharField(max_length=1, choices=STUDENT_HISPANIC_CHOICES, default=NO, null=True)

    def __unicode__(self):
        return '%s' % self.student_id


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
    student_id = models.ForeignKey('Student', to_field='student_id', null=True)
    #Native ID number used at the organization
    student_odd_id = models.CharField(max_length=25, null=True)
    student_odd_networkid = models.CharField(max_length=25, null=True)
    student_odd_enrollstatus = models.CharField(max_length=1, choices=STUDENT_ODD_ENROLLSTATUS_CHOICES, null=True)
    student_odd_housingelig = models.CharField(max_length=1, choices=STUDENT_ODD_HOUSINGELIG_CHOICES, null=True)
    student_odd_undergradlevel = models.CharField(max_length=1, choices=STUDENT_ODD_UNDERGRADLEVEL_CHOICES, null=True)
    #TODO: Filter and precalc ODD so that queries hit this table and can batch load academic data
    student_odd_major = models.CharField(max_length=50, null=True)
    student_odd_major2 = models.CharField(max_length=50, null=True)
    student_odd_minor = models.CharField(max_length=50, null=True)
    student_odd_minor2 = models.CharField(max_length=50, null=True)
    student_odd_credits = models.DecimalField(default=Decimal('0.00'), max_digits=5, decimal_places=2, null=True)
    student_odd_gpa = models.DecimalField(default=Decimal('0.0000'), max_digits=5, decimal_places=4, null=True)

    def __unicode__(self):
        return '%s' % self.student_id


class Student_contact_oncampus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id', null=True)
    student_phone_main_countrycode = models.CharField(max_length=2, null=True)
    student_phone_main_digits = models.CharField(max_length=16, null=True)
    student_phone_main_ext = models.CharField(max_length=8, null=True)
    student_phone_2_countrycode = models.CharField(max_length=2, null=True)
    student_phone_2_digits = models.CharField(max_length=16, null=True)
    student_phone_2_ext = models.CharField(max_length=8, null=True)
    #TODO: Link oncampus data to housing module

    def __unicode__(self):
        return '%s' % self.student_id


class Student_contact_offcampus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id', null=True)
    student_offcampus_country = models.CharField(max_length=100, null=True)
    student_offcampus_region = models.CharField(max_length=100, null=True)
    student_offcampus_city = models.CharField(max_length=100, null=True)
    student_offcampus_postcode = models.CharField(max_length=16, null=True)
    student_offcampus_street = models.CharField(max_length=50, null=True)
    student_offcampus_streetnumber = models.IntegerField(null=True)
    student_offcampus_boxnumber = models.CharField(max_length=4, null=True)

    def __unicode__(self):
        return '%s' % self.student_id


class Student_contact_emergency(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id', null=True)
    student_emergency_1_name_first = models.CharField(max_length=64, null=True)
    student_emergency_1_name_last = models.CharField(max_length=64, null=True)
    student_emergency_1_name_middle = models.CharField(max_length=64, null=True)
    student_emergency_1_name_suffix = models.CharField(max_length=4, null=True)
    student_emergency_1_country = models.CharField(max_length=100, null=True)
    student_emergency_1_region = models.CharField(max_length=100, null=True)
    student_emergency_1_city = models.CharField(max_length=100, null=True)
    student_emergency_1_postcode = models.CharField(max_length=16, null=True)
    student_emergency_1_street = models.CharField(max_length=50, null=True)
    student_emergency_1_streetnumber = models.IntegerField(null=True)
    student_emergency_1_boxnumber = models.CharField(max_length=4, null=True)
    student_emergency_1_phone_countrycode = models.CharField(max_length=2, null=True)
    student_emergency_1_phone_digits = models.CharField(max_length=16, null=True)
    student_emergency_1_phone_ext = models.CharField(max_length=8, null=True)
    student_emergency_2_name_first = models.CharField(max_length=64, null=True)
    student_emergency_2_name_last = models.CharField(max_length=64, null=True)
    student_emergency_2_name_middle = models.CharField(max_length=64, null=True)
    student_emergency_2_name_suffix = models.CharField(max_length=4, null=True)
    student_emergency_2_country = models.CharField(max_length=100, null=True)
    student_emergency_2_region = models.CharField(max_length=100, null=True)
    student_emergency_2_city = models.CharField(max_length=100, null=True)
    student_emergency_2_postcode = models.CharField(max_length=16, null=True)
    student_emergency_2_street = models.CharField(max_length=50, null=True)
    student_emergency_2_streetnumber = models.IntegerField(null=True)
    student_emergency_2_boxnumber = models.CharField(max_length=4, null=True)
    student_emergency_2_phone_countrycode = models.CharField(max_length=2, null=True)
    student_emergency_2_phone_digits = models.CharField(max_length=16, null=True)
    student_emergency_2_phone_ext = models.CharField(max_length=8, null=True)

    def __unicode__(self):
        return '%s' % self.student_id


#Student_resident_oncampus_current will define all relationships between student and bed
#TODO: Create resident_timecode table as part of a system Vars table. Orgs store pre-defined start-end dates for semesters
class Student_resdata_oncampus (models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey('Student', to_field='student_id', null=True)
    #TODO: Create building table
    building_id = models.ForeignKey('Building', to_field='building_id', null=True)
    floor_id = models.ForeignKey('Building_floor', to_field='floor_id', null=True)
# Note: do we need to many-many the building objects?
# Seems enough to many-many student and bed, then cascade up to rm, fl, bldg

#    building_id_rel = models.ManyToManyField('Building')
#    floor_id = models.ManyToManyField('Building_floor', to_field='floor_id')
#    room_id = models.ManyToManyField('Building_room', to_field='room_id')
#    bed_id = models.ManyToManyField('Building_room_bed', to_field='bed_id')
#    resident_timecode_id = models.ManyToManyField('Vars_resident_timecode', to_field='resident_timecode_id')


class Building (models.Model):
    YES = '1'
    NO = '0'

    BUILDING_ISTESTDATA_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    istestdata = models.CharField(max_length=1, choices=BUILDING_ISTESTDATA_CHOICES, default=YES, null=True)
    building_id = models.CharField(max_length=16, unique=True, null=True)
    building_name = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return '%s' % self.building_id


class Building_floor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    building_id = models.ForeignKey('Building', to_field='building_id', null=True)
    floor_id = models.CharField(max_length=16, unique=True, null=True)
    floor_name = models.CharField(max_length=32, null=True)
    floor_vertical_heightnumber = models.IntegerField(null=True)

    def __unicode__(self):
        return '%s' % self.floor_id


class Building_room(models.Model):

    FEMALE = '1'
    MALE = '2'
    TRANS = '3'
    CIS = '4'

    STUDENT_GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (TRANS, 'Trans'),
        (CIS, 'Cis')
    )
   #TODO: need to find details on accessibility options for room
    STUDENT_ACCESSIBLE_CHOICES = (

    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    building_id = models.ForeignKey('Building', to_field='building_id', null=True)
    floor_id = models.ForeignKey('Building_floor', to_field='floor_id', null=True)
    room_id = models.CharField(max_length=8, unique=True, null=True)
    room_name = models.CharField(max_length=16, null=True)
    room_param_gender = models.CharField(max_length=2, choices=STUDENT_GENDER_CHOICES, null=True)
    room_param_accessible = models.CharField(max_length=2, choices=STUDENT_ACCESSIBLE_CHOICES, null=True)

    def __unicode__(self):
        return '%s' % self.room_id


class Userextn_user(models.Model):
    YES = '1'
    NO = '0'

    USEREXTN_USER_ISTESTDATA_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    istestdata = models.CharField(max_length=1, choices=USEREXTN_USER_ISTESTDATA_CHOICES, null=True, default=YES)
    #user_firstname =


class Userextn_admin(models.Model):

    YES = '1'
    NO = '0'

    USEREXTN_ADMIN_ISTESTDATA_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    istestdata = models.CharField(max_length=1, choices=USEREXTN_ADMIN_ISTESTDATA_CHOICES, null=True, default=YES)

    def __unicode__(self):
        return '%s' % self.user

class userextn_photos(models.Model):

    YES = '1'
    NO = '0'

    USEREXTN_ADMIN_ISTESTDATA_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_edited = models.DateTimeField(auto_now=True)
    istestdata = models.CharField(max_length=1, choices=USEREXTN_ADMIN_ISTESTDATA_CHOICES, null=True, default=YES)
    user_img = models.ImageField(upload_to='users')
