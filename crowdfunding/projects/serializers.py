from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'
        

class PledgeDetailSerializer(PledgeSerializer):
  
  
  def update(self, instance, validated_data):
       instance.title = validated_data.get('title', instance.title)
       instance.description = validated_data.get('description', instance.description)
       instance.goal = validated_data.get('goal', instance.goal)
       instance.image = validated_data.get('image', instance.image)
       instance.is_open = validated_data.get('is_open', instance.is_open)
       instance.date_created = validated_data.get('date_created', instance.date_created)
       instance.owner = validated_data.get('owner', instance.owner)
       instance.save()
       return instance


# The ModelSerializer class already knows how to convert a model instance into JSON!
class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    # The only customisation that we need to do is to tell it which model to convert, class Meta: block is doing
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'
        # We tell our new serializer that its job is to serialize our Project model into JSON, and that it should include __all__ of the fields when it does so!

class ProjectDetailSerializer(ProjectSerializer):
   pledges = PledgeSerializer(many=True, read_only=True)
   
   
   def update(self, instance, validated_data):
       instance.title = validated_data.get('title', instance.title)
       instance.description = validated_data.get('description', instance.description)
       instance.goal = validated_data.get('goal', instance.goal)
       instance.image = validated_data.get('image', instance.image)
       instance.is_open = validated_data.get('is_open', instance.is_open)
       instance.date_created = validated_data.get('date_created', instance.date_created)
       instance.owner = validated_data.get('owner', instance.owner)
       instance.save()
       return instance
   

