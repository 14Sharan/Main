from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Subjects(request):
    return render(request, "subjects/subjects-list.html")