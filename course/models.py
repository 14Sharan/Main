from django.db import models

# Create your models here.


class Subjects(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    subject_image = models.FileField(upload_to='subject_image',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        db_table = "tbl_subjects"


class CourseVideos(models.Model):
    video = models.FileField(upload_to='course_video',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
        db_table = "tbl_course_video"



class Course(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    decription=models.CharField(max_length=255,null=True,blank=True)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE,null=True,blank=True)
    image = models.FileField(upload_to = 'course_image',null=True,blank=True)
    preview_video = models.FileField(upload_to='preview_video',null=True,blank=True)
    course_video = models.ManyToManyField(CourseVideos)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        db_table = "tbl_course"

