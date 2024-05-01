from django.contrib import admin

# Register your models here.
# from .models import Contact
# from .models import Student_detail

from app.models import *

admin.site.register(Contact)
admin.site.register(Student_detail)

admin.site.register(About_Me)

admin.site.register(Stu_manage)
