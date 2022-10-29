from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from courses.models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses/index.html', context)

def detail(request, course_id):
    course_detail = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course_detail,
    }
    return render(request, 'courses/detail.html', context)
