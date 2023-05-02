from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeesViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeesViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
