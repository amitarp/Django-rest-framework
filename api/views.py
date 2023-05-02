from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Employees
from .serializers import CompanySerializer,EmployeesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=CompanySerializer

    #for custom APIS
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employees.objects.filter(company=company)
            emps_serializer=EmployeesSerializer(emps,many=True,context={'request':request})
        except Exception as e:
            return Response({
                'message':'Company does not exist'
            })

        return Response(emps_serializer.data)

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class=EmployeesSerializer