# from django.db import models


# class school(models.Model):
#     name = models.CharField(max_length=200,default= "",null=False,blank=False)
#     description = models.CharField(max_length=200, default="", null=False, blank=False)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
# class Meta(object):
#         verbose_name_plural = 'School'
#         verbose_name = 'School'
# class department(models.Model):
#     school = models.ForeignKey(school, on_delete=models.CASCADE,related_name='related_medicine')
#     name = models.CharField(max_length=200,default= "",null=False,blank=False)
#     description = models.CharField(max_length=200, default="", null=False, blank=False)
#     date_created = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.name
# class Meta(object):
#         verbose_name_plural = 'Department'
#         verbose_name = 'Department'

# class subject(models.Model):
#     department = models.ForeignKey(department, on_delete=models.CASCADE,related_name='related_medicine')
#     name = models.CharField(max_length=200,default= "",null=False,blank=False)
#     description = models.CharField(max_length=200, default="", null=False, blank=False)
#     date_created = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.name
# class Meta(object):
#         verbose_name_plural = 'Subject'
#         verbose_name = 'Subject'
# class question(models.Model):
#     subject = models.ForeignKey(subject, on_delete=models.CASCADE,related_name='related_medicine')
#     statement = models.CharField(max_length=200,default= "",null=False,blank=False)
#     description = models.CharField(max_length=200, default="", null=False, blank=False)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.statement
# #dashboard name is 'Product'
#     class Meta(object):
#         verbose_name_plural = 'Question'
#         verbose_name = 'Question'


# class answer(models.Model):
#     question = models.ForeignKey(question, on_delete=models.CASCADE,related_name='related_medicine')
#     statement = models.CharField(max_length=200,default= "",null=False,blank=False)
#     description = models.CharField(max_length=200, default="", null=False, blank=False)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.statement
# #dashboard name is 'Product'
#     class Meta(object):
#         verbose_name_plural = 'Answer'
#         verbose_name = 'Answer'
