from app01 import models
from rest_framework.views import APIView
# from api.utils.response import BaseResponse
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.serializers.course import DegreeCourseSerializer


# 查询所有学位课程

class DegreeCourseView(APIView):

    def get(self,request,*args,**kwargs):
        response = {'code':100,'data':None,'error':None}

        try:
            # 从数据库获取数据
            degreecourse_list = models.DegreeCourse.objects.all()

            # 分页
            # page = PageNumberPagination()
            # course_list = page.paginate_queryset(queryset,request,self)

            # 分页之后的结果执行序列化
            ser_obj = DegreeCourseSerializer(degreecourse_list,many=True)

            response['data'] = ser_obj.data
        except Exception as e:

            response['error'] = '获取数据失败'

        return Response(response)




class DegreeCourseDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        response = {'code': 100, 'data': None, 'error': None}
        try:
            degree_course = models.DegreeCourse.objects.filter(id=pk).first()

            ser = DegreeCourseSerializer(degree_course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)


