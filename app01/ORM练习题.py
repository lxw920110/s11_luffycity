from django.shortcuts import render,HttpResponse

from app01 import models


# Create your views here.


def index(request):
# ORM练习
# a.查看所有学位课并打印学位课名称以及授课老师
    degree_list = models.DegreeCourse.objects.all().values('name','teachers__name')
    print(degree_list)
    queryset = models.DegreeCourse.objects.all()
    for row in queryset:
        row.name,row.teachers.all()



# b.查看所有学位课并打印学位课名称以及学位课的奖学金
    degree_list = models.DegreeCourse.objects.all()
    for row in degree_list:
        scholoarships = row.scholarship_set.all()
        for item in scholoarships:
            print(item.time_percent,item.value)





# c.展示所有的专题课
    course_list = models.Course.filter(degree_course__isnull = True)
    print(course_list)



# d.查看id = 1
# 的学位课对应的所有模块名称
    course_list = models.DegreeCourse.objects.filter(id = 1).values('course__name')
    print(course_list)

    course_list = models.Course.objects.filter(degree_course_id = 1)
    print(course_list)


# e.获取id = 1
# 的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    course_list = models.Course.objects.filter(id = 1)
    print(course_list.values('name'))
    print(course_list.first().get_level_display())
    print(course_list.values('coursedetail__why_study'))
    print(course_list.values('coursedetail__what_to_study_brief'))
    print(course_list.values('coursedetail__recommend_courses'))

    obj = models.Course.objects.get(id = 1)
    print(obj.name)
    print(obj.brief)
    print(obj.get_level_display())
    print(obj.coursedetail.hours)
    print(obj.coursedetail.why_study)
    print(obj.coursedetail.recommend_courses.all())



# f.获取id = 1
# 的专题课，并打印该课程相关的所有常见问题
    c_obj = models.Course.objects.filter(degree_course__isnull = True,id = 1).first()
    print(c_obj.asked_question.all().values('question'))

    obj = models.Course.objects.get(degree_course__isnull = True,id = 1)
    ask_list = obj.asked_question.all()
    for item in ask_list:
        print(item.question,item.answer)




# g.获取id = 1
# 的专题课，并打印该课程相关的课程大纲
    c_obj = models.Course.objects.filter(degree_course__isnull = True,id = 1)
    print(c_obj.values('coursedetail__courseoutline__title'))

    c_obj = models.Course.objects.get(id = 1)
    outline_list = c_obj.coursedetail.courseoutline_set.all()
    for item in outline_list:
        print(item.title,item.content)


# h.获取id = 1
# 的专题课，并打印该课程相关的所有章节
    c_obj = models.Course.objects.filter(degree_course__isnull = True,id = 1)
    print(c_obj.values('coursechapters__name'))

    obj = models.Course.objects.get(degree_course__isnull = True,id = 1)
    chapter_list = obj.coursechapters.all()
    for item in chapter_list:
        print(item.name)



# i.获取id = 1
# 的专题课，并打印该课程相关的所有课时
    c_obj = models.Course.objects.filter(id = 1)
    print(c_obj.values('coursechapters__name'))

    obj = models.Course.objects.get(id = 1)
    chapter_list = obj.coursechapters.all()
    for obj in chapter_list:
        print(obj.name)


    c_obj = models.Course.objects.filter(id = 1)
    for i in c_obj.values('coursechapters__chapter','coursechapters__name'):
        print(i.get('coursechapters__chapter'),i.get('coursechapters__name'))
        a_obj = models.CourseChapter.objects.filter(name = i.get('coursechapters__name'))
        for j in a_obj.values('coursesections__name'):
            print(j.get('coursesections__name'))







    return HttpResponse('OK')


