from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_date):
        company = Company(
            company_name=validated_date['company_name'], email=validated_date['email'])
        company.set_password(validated_date['password'])
        company.save()
        return company
