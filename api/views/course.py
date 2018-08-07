from app01 import models
from rest_framework.views import APIView
from api.utils.response import BaseResponse
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.serializers.course import CourseModelSerializer


# 查询所有专题课程

class CoursesView(APIView):

    def get(self,request,*args,**kwargs):
        response = {'code':100,'data':None,'error':None}

        try:
            # 从数据库获取数据
            queryset = models.Course.objects.all()

            print(queryset)

            # 分页
            # page = PageNumberPagination()
            # course_list = page.paginate_queryset(queryset,request,self)

            # 分页之后的结果执行序列化
            ser = CourseModelSerializer(queryset,many=True)

            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'

        return Response(response)




class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)


