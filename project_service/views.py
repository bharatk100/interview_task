from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer


class ProjectView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            project_obj = Project.objects.get(id=pk, user=request.user)
            if project_obj:
                serializer = ProjectSerializer(project_obj, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error": "project object not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            project_obj = Project.objects.get(id=pk)
            serializer = ProjectSerializer(project_obj)
            return Response(serializer.data)
        except ProjectSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    def patch(self, request, pk):
        try:
            project_obj = Project.objects.get(id=pk, user=request.user)
            if project_obj:
                serializer = ProjectSerializer(project_obj, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error": "project object not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            project_obj = Project.objects.get(id=pk, user=request.user)
            project_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response({"error":"project object not found"}, status=status.HTTP_404_NOT_FOUND)



