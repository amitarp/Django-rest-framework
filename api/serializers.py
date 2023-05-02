from rest_framework import serializers
from .models import Company,Employees

#create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:

        model=Company
        fields="__all__"

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employees
        fields="__all__"

