from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from course.models import *


@login_required
def AllSubjects(request):
    subjects=Subjects.objects.all().order_by('-id')
    return render(request, "subjects/subjects-list.html",{"subjects":subjects})


@login_required
def AddSubject(request):
    if request.method == "GET":
        return render(request,"subjects/add-subject.html")
    if request.method == "POST":
        Subjects.objects.create(title=request.POST.get('title'),
                                description = request.POST.get('description'),
                                subject_image = request.FILES.get('subject_image'))
        return redirect('course:add_subject')
    
@login_required
def EditSubject(request,id):
    subject = Subjects.objects.get(id=id)
    if request.method == "GET":
        return render(request,"subjects/edit-subject.html",{"subject":subject})
    if request.method == "POST":
        if request.POST.get('title'):
            subject.title = request.POST.get('title')
        if request.POST.get('description'):
            subject.description = request.POST.get('description')
        if request.FILES.get('title'):
            subject.subject_image = request.FILES.get('subject_image')
        subject.save()
        return redirect("course:subjects")
    
@login_required
def DeleteSubject(request,id):
    Subjects.objects.get(id=id).delete()
    return redirect('course:subjects')



@login_required
def CourseList(request):
    course = Course.objects.all().order_by('-created_on')
    return render(request,"admin/course/course-list.html",{"courses":course})

@login_required
def AddCourse(request):
    subjects= Subjects.objects.all().order_by('-created_on')
    if request.method == "GET":
        return render(request,"admin/course/add-course.html",{"subjects":subjects})
    if request.method== "POST":
        course=Course.objects.create(title = request.POST.get('title'),
                            description = request.POST.get("description"),
                            image=request.FILES.get("course_image"),
                            subject_id = request.POST.get('subjects'),
                            preview_video = request.FILES.get("pre_video"),
                            )

        return redirect("course:add_course")


@login_required
def ViewCourse(request):
    return render(request,"admin/course/view-course.html")