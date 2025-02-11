from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly, IsSuperUser

from django.http import Http404
from .models import Project, Pledge
from .serializers import PledgeDetailSerializer, ProjectSerializer, PledgeSerializer, ProjectDetailSerializer , UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from django.db.models import Sum




class ProjectList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # parser_classes = [MultiPartParser, FormParser]
# Permission allows any user (authenticated or not) to view the project list, but only authenticated users can create a new project (POST).

    def get(self, request):
       projects = Project.objects.all()
       serializer = ProjectSerializer(projects, many=True)
       return Response(serializer.data)
   
  
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Q: how about showing project list only by name? owner? A: it's happening already in project list. in projectdetails we will see the details.
 

class ProjectDetail(APIView):
    
    
    permission_classes = [
      permissions.IsAuthenticatedOrReadOnly,
      IsOwnerOrReadOnly | IsSuperUser]
    # parser_classes = [MultiPartParser, FormParser]

# Project details are visible to all users, but only the owner or admin can edit the project.


    def get_object(self, pk):
       
       try:
           project = Project.objects.get(pk=pk)
           self.check_object_permissions(self.request, project)
           return project
       except Project.DoesNotExist:
           raise Http404("Project not found.")
       


    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
   
        

    def put(self, request, pk):
       project = self.get_object(pk)
       serializer = ProjectDetailSerializer(
           instance=project,
           data=request.data,
           partial=True
        )
    
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)

       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
           )
    
# to avoid problems the delete is not applied, instead the owner can close the project.

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response( {"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
 


# Anyone can get the list of pledges, but only authenticated users can create a pledge.
# there's some logic check to see if the project goal is met project don't accept new pledges, if the latest supporter is exceeding the amount for the goal in the last pledge it will be prompted by the right amount, it could be addressed later in REACT but just wanted to apply complex logic in API.



class PledgeList(APIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            project_id = request.data.get('project')

            # 1- Retrieve the project instance
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                return Response({'detail': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)

            # 2- Check if the project is already closed
            if not project.is_open:
                return Response({'detail': 'This project is closed and no longer accepts pledges.'}, status=status.HTTP_400_BAD_REQUEST)

            # 3- Calculate the total pledge amount for the project

            pledges = Pledge.objects.filter(project_id=project_id)
            total_pledge_amount = pledges.aggregate(total=Sum('amount'))['total'] or 0

            # 4- Calculate the remaining amount needed to reach the goal
            remaining_amount = project.goal - total_pledge_amount

            # 5- Check if the pledge amount exceeds the remaining amount needed to reach the goal
            pledge_amount = serializer.validated_data['amount']  # Get the amount of the current pledge

            if pledge_amount > remaining_amount:
                # If the pledge exceeds the remaining amount, only allow the remaining amount to be pledged
                return Response(
                    {'detail': f'The maximum pledge you can make is {remaining_amount} to fully fund the project.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # 6- If the pledge is valid, save the pledge
            pledge = serializer.save(supporter=request.user)

            # 7- Recalculate the total pledge amount after this pledge and close the project if necessary
            total_pledge_amount += pledge_amount
            print("")
            if total_pledge_amount >= project.goal:
                project.is_open = False 
                project.completed = True # Close the project
                project.save()

                print(project.completed)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



# only the pledgeowner or supporter can update the pledge details.   
class PledgeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , IsSupporterOrReadOnly]
    

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404("Pledge not found.")

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)
    

    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # This should return a Response object
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # And this as well
    
    def delete(self, request, pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(
             {"detail": "Pledge successfully deleted"},
            status=status.HTTP_200_OK
        )

    

class UserProfileView(RetrieveAPIView):
    '''
    show a profile of each user including projects and pledges.
    '''
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_object(self):
        return self.request.user
    


    