from rest_framework import serializers
from . models import cardetails

class detailsSerializer(serializers.ModelSerializer):
	class Meta:
		model=cardetails
		field='__all__'