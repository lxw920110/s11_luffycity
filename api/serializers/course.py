from rest_framework import serializers
from app01 import models


class CourseModelSerializer(serializers.ModelSerializer):

    level_name = serializers.CharField(source='get_level_display',read_only=True)
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    why_study = serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief = serializers.CharField(source = 'coursedetail.what_to_study_brief')





    # 多对多
    recommend_courses = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    outline = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()


    class Meta:
        model = models.Course
        fields = ['__all__']

    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [ {'id':item.id,'name':item.name} for item in recommend_list]

    def get_question(self,row):
        question_list = row.asked_question.all()
        print(question_list)
        return [{'question':item.question,'answer':item.answer} for item in question_list]

    def get_outline(self,row):
        outline_list = row.coursedetail.courseoutline_set.all()
        return [{'title':item.title} for item in outline_list]

    def get_chapter(self,row):
        chapter_list = row.coursechapters.all()
        return [{'name':item.name} for item in chapter_list]


class DegreeCourseSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    scholarship = serializers.SerializerMethodField()


    class Meta:
        model = models.DegreeCourse
        fields = ['name','teachers','scholarship']

    def get_teachers(self,row):
        teacher_list = row.teachers.all()
        return [{'name':teacher.name} for teacher in teacher_list]

    def get_scholarship(self,row):
        scholarship_list = row.scholarship_set.all()
        return [{'value':scholarship.value} for scholarship in scholarship_list]






