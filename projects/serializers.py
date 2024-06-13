from rest_framework import serializers
from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        read_only_fields = ('created_at', )
