from django.conf.urls import url
from api.views import course,degreecourse



urlpatterns = [
    url(r'courses/$',course.CoursesView.as_view()),
    url(r'courses/(?P<pk>\d+)/$',course.CourseDetailView.as_view()),
    url(r'degreecourses/$',degreecourse.DegreeCourseView.as_view()),
    url(r'degreecourses/(?P<pk>\d+)/$',degreecourse.DegreeCourseDetailView.as_view()),
]