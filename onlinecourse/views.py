from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404

# subclass of django listview
class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'
    # Override get_queryset()
    def get_queryset(self):
       courses = Course.objects.order_by('-total_enrollment')[:10]
       return courses
# sample of django baseview
# class CourseListView(View):
#     def get(self, request):
#         context = {}
#         #list top5 model.course
#         course_list = Course.objects.order_by('-total_enrollment')[:10]
#         #convert to dict structure
#         context['course_list'] = course_list
#         return render(request, 'onlinecourse/course_list.html', context)

class EnrollView(View):
    # Handles post request
    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('pk')
        #TRY get, EXCEPT raise 404error
        course = get_object_or_404(Course, pk=course_id)
        # Increase total enrollment by 1
        course.total_enrollment += 1
        course.save()
        #viewname=(url name)
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

# subclass of django detailview
class CourseDetailsView(generic.DetailView):
    model = Course
    #html template
    template_name = 'onlinecourse/course_detail.html'
