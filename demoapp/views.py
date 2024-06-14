from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Task
from rest_framework import generics
from.serializer import Taskserializer

@api_view(['GET'])
def list(request):
    task=Task.objects.all()
    serializer=Taskserializer(task,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer=Taskserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
   
@api_view(['GET'])
def details(request,pk):
    task=Task.objects.get(id=pk)
    serializer=Taskserializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    task=Task.objects.get(id=pk)
    serializer=Taskserializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
   
    return Response('item deleted')
