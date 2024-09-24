from django.db import models
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


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )