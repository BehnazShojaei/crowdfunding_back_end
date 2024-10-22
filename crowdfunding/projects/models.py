from django.db import models
from django.contrib.auth import get_user_model
# inherited our class from the built-in models.Model class
class Project(models.Model):

#  Each of these is itself an instance of one of the classes that comes bundled with Django. These attributes tell Django what types of fields we want in our database table.
# We can pass arguments to our model's field attributes to specify extra functionality
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Relationship between user and projects, as each user can make many projects, the related name will be in user table as a property
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )
    completed = models.BooleanField(default=False)  

    # how to close the pledge where to add the logic to check this?
    # @property
    # def total_amount(self):
    #     return self.pledges.aggregate(sum=models.Sum('amount'))['sum'] or 0
    # # 0 to replace None when there's no pledges

    # @property
    # def total_amount(self):
    #     total = self.pledges.aggregate(sum=models.Sum('amount'))['sum'] or 0
    #     print(f'Total amount pledged: {total}')
    #     return total


    # def close_if_goal_met(self):
    #     if self.total_amount >= self.goal:
    #         self.is_open = False
    #         self.save()
        
    def close_if_goal_met(self):
        if self.is_open and self.total_amount >= self.goal:
            print(f'Closing project {self.title} as total amount {self.total_amount} has met or exceeded the goal {self.goal}.')
            self.is_open = False
            self.save()
   
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
    #what if someone choose yes/no to anonymous questeion? I think we need to check it to show the supporter name or not