import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Device, DeviceLog
from .serializers import DeviceSerializer, DeviceLogSerializer

# Create your views here.


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def add_device(request):
    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['company'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def device_list(request):
    if request.method == 'GET':
        # Retrieve the employees belonging to the authenticated company
        device = Device.objects.filter(company=request.user)
        serializer = DeviceSerializer(device, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_log(request):
    if request.method == 'POST':
        serializer = DeviceLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['company'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def log_list(request):
    if request.method == 'GET':
        device_log = DeviceLog.objects.filter(company=request.user)
        serializer = DeviceLogSerializer(device_log, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def return_device(request):
    log_id = request.data.get('id')
    returned_condition = request.data.get('returned_condition')
    if request.method == 'POST':
        log = get_object_or_404(DeviceLog, id=log_id)
        log.returned_date = datetime.datetime.now()
        log.returned_condition = returned_condition
        log.save()
        return Response({'message': 'Device returned successfully.'}, status=status.HTTP_200_OK)
