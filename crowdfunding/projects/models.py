from django.db import models
from django.contrib.auth import get_user_model
# inherited our class from the built-in models.Model class
class Project(models.Model):

#  Each of these is itself an instance of one of the classes that comes bundled with Django. These attributes tell Django what types of fields we want in our database table.
# We can pass arguments to our model's field attributes to specify extra functionality
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Relationship between user and projects, as each user can make many projects, the related name will be in user table as a property
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )
    completed = models.BooleanField(default=False)  

   
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    # Relationship between user and pledges, as each user can make many pledges, the related name will be in user table as a property
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    #I can add the above supporter as supporter_private and add a supporter_public 
    #pledge doesn't want date?
    #what if someone choose yes/no to anonymous questeion? I think we need to check it to show the supporter name or not, is it happening at REACT?