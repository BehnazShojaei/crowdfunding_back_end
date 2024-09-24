from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'
# The ModelSerializer class already knows how to convert a model instance into JSON!
class ProjectSerializer(serializers.ModelSerializer):
    # The only customisation that we need to do is to tell it which model to convert, class Meta: block is doing
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'
        # We tell our new serializer that its job is to serialize our Project model into JSON, and that it should include __all__ of the fields when it does so!
