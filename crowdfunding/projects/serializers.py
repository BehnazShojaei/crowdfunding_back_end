from rest_framework import serializers
from django.apps import apps
from django.contrib.auth import get_user_model


class PledgeSerializer(serializers.ModelSerializer):
    

    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

    def get_supporter(self, obj):
        if obj.anonymous:
            return "Anonymous"
        return obj.supporter.username
    # ask if it is the right place to add logic checking anonymous?

        

class PledgeDetailSerializer(PledgeSerializer):
    

  def update(self, instance, validated_data):
       instance.amount = validated_data.get('amount', instance.amount)
       instance.comment = validated_data.get('comment', instance.comment)
       instance.anonymous = validated_data.get('anonymous', instance.anonymous)
    #    instance.project = validated_data.get('project', instance.project)
    #    instance.date_created = validated_data.get('date_created', instance.date_created)
    #    instance.owner = validated_data.get('owner', instance.owner)
       instance.save()
       return instance
#   should i add update for project as well?



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
       instance.image_b64 = validated_data.get('image', instance.image_b64)

       instance.is_open = validated_data.get('is_open', instance.is_open)
       instance.date_created = validated_data.get('date_created', instance.date_created)
       instance.completed = validated_data.get('completed', instance.completed)

    #    in real life a user would not need to change the owner! however in insomnia I had this option activated when puplating data
    #  instance.owner = validated_data.get('owner', instance.owner)
    
       instance.save()
       return instance
      

class UserProfileSerializer(serializers.ModelSerializer):
    owned_projects = ProjectSerializer(many=True, read_only=True)
    pledges = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'owned_projects', 'pledges']