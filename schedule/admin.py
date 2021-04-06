from django.contrib import admin
from .models import Classes,ClassTeachers, Students,Teachers
# Register your models here.
class ClassTeachersAdmin(admin.ModelAdmin):
    horizontal_filter = ['Teachers']
    search_fields=['teacher_name']

admin.site.register(Classes)
admin.site.register(ClassTeachers,ClassTeachersAdmin)
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.site_title="Web Dev for KCGS"
admin.site.site_header="KCGS ISEYIN"
admin.site.index_title="Welcome To KCGS ISEYIN"
