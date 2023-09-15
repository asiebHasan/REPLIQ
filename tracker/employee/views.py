from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            # Ensuring employee belongs to the company
            if serializer.validated_data['company'] == request.user:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid company for the employee'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_list(request):
    if request.method == 'GET':
        # Retrieve the employees belonging to the authenticated company
        employees = Employee.objects.filter(company=request.user)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
