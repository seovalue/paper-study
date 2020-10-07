from django.shortcuts import render
from .models import Movie
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer

# Create your views here.
c