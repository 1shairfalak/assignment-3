from unicodedata import category
from rest_framework import serializers
from rest_framework.response import Response
from .models import *

class schoolSerilizer(serializers.ModelSerializer):
    class Meta:
        model = school
        fields = ( 'name','description','date_created')
class departmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ( 'school','name','description','date_created')

class subjectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ( 'department','name','description','date_created')

class questionSerilizer_(serializers.ModelSerializer):
    class Meta:
       model = question
       fields = ( 'description','date_created')
class questionSerilizer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name', read_only=True)
    subject_description = serializers.CharField(source='subject.description', read_only=True)
   
    class Meta:
        model = question
        fields = ( 'subject','subject_description','statement','description','date_created')



class questionwithdepartmentSerilizer(serializers.ModelSerializer):
    department = serializers.CharField(source='subject.department.name', read_only=True)
    subject = serializers.CharField(source='subject.name', read_only=True)
    subject_description = serializers.CharField(source='subject.description', read_only=True)
   
    class Meta:
        model = question
        fields = ( 'subject','subject_description','statement','description','date_created','department')



class questionhierarchySerilizer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='subject.department.school.name', read_only=True)
    department_name = serializers.CharField(source='subject.department.name', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
   
   
    class Meta:
        model = question
        fields = ( 'school_name','department_name','subject_name','statement','description','date_created')

class questionfilterSerilizer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name', read_only=True)
    
    class Meta:
        model = question
        fields = ['subject','statement','description','date_created']