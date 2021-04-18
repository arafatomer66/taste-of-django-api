from django.shortcuts import render
from .models import Project
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/project-list/'
    }

    return Response(api_urls)


@api_view(['GET'])
def showAll(request):
    projects = Project.objects.all()
    serializer = ProductSerializer(projects, many=True)
    return Response(serializer.data)
