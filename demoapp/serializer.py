from.models import Task
from rest_framework import serializers

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        