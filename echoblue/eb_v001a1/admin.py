from django.contrib import admin

from .models import Organization
from .models import Organization_children
from .models import Organization_description
from .models import Organization_location
from .models import Student
from .models import Student_contact_offcampus
from .models import Student_contact_oncampus
from .models import Student_odd
from .models import Student_demogdata
from .models import Student_contact_emergency
from .models import Student_resdata_oncampus
from .models import Building
from .models import Building_floor
from .models import Building_room
from .models import Userextn_admin


admin.site.register(Organization)
admin.site.register(Organization_children)
admin.site.register(Organization_location)
admin.site.register(Organization_description)
admin.site.register(Student)
admin.site.register(Student_contact_offcampus)
admin.site.register(Student_contact_oncampus)
admin.site.register(Student_odd)
admin.site.register(Student_demogdata)
admin.site.register(Student_contact_emergency)
admin.site.register(Student_resdata_oncampus)
admin.site.register(Building)
admin.site.register(Building_floor)
admin.site.register(Building_room)
admin.site.register(Userextn_admin)

