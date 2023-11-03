from django.shortcuts import render
from rest_framework.generics import ListAPIView
from app.models import Student
from app.serializers import StudentSerializer
from app.pagination import MyPageNumberPagination
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentPaginationApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination











