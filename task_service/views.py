from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class TaskView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        priority = self.request.query_params.get('priority')
        status = self.request.query_params.get('status')
        due_date = self.request.query_params.get('due_date')
        all_tasks = Task.objects.all()
        if priority:
            all_tasks = all_tasks.filter(priority=priority)
        if status:
            all_tasks = all_tasks.filter(status=status)
        if due_date:
            all_tasks = all_tasks.filter(due_date=due_date)
        all_tasks = all_tasks.order_by("priority", "status", "due_date")
        serializer = TaskSerializer(all_tasks, many=True)
        return Response(serializer.data)
        # try:
        #     task_obj = Task.objects.get(id=pk)
        #     serializer = TaskSerializer(task_obj)
        #     return Response(serializer.data)
        # except Task.DoesNotExist:
        #     return Response({"msg":"data not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            task_obj = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({"msg":"data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task_obj, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def patch(self, request, pk):
        try:
            task_obj = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response({"msg":"data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            task_obj = Task.objects.get(id=pk, user=request.user)
            task_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error":"data not found"}, status=status.HTTP_404_NOT_FOUND)        
        
