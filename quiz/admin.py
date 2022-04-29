from django.contrib import admin
from .models import *

# class answer_(admin.ModelAdmin):
#     fields  = "__all__"
class question_(admin.ModelAdmin):
     fields = ( 'subject','statement','description')
class subject_(admin.ModelAdmin):
    fields = ( 'department','name','description')
class department_(admin.ModelAdmin):
     fields = ( 'school','name','description')
class school_(admin.ModelAdmin):
    fields = ( 'name','description')

  
 
# admin.site.register(answer,answer_)
admin.site.register(school, school_)
admin.site.register(question, question_)
admin.site.register(subject, subject_)
admin.site.register(department, department_)
