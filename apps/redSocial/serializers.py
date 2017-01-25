from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from apps.redSocial.models import AreaConocimiento

class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','email')

class AreaConocimientoSerializer(ModelSerializer):
	class Meta:
		model = AreaConocimiento
		fields = ('descripcion','estatus')