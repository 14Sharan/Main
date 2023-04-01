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
