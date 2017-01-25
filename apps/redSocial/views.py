from django.shortcuts import render
from django.contrib.auth.models import User
from apps.redSocial.models import AreaConocimiento
from rest_framework import viewsets
from apps.redSocial.serializers import UserSerializer, AreaConocimientoSerializer

class UserViewSet(viewsets.ModelViewSet):
	""""
	API endpoint that allows users to be viewed or edited
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class AreaConocimientoViewSet(viewsets.ModelViewSet):
	""""
	API endpoint that allows users to be viewed or edited
	"""
	queryset = AreaConocimiento.objects.all()
	serializer_class = AreaConocimientoSerializer
	