from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
# ChangePasswordSerializer, CustomUserDetailSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# from projects.permissions import IsUserOrBanished

class CustomUserList(APIView):
  def get(self, request):
      users = CustomUser.objects.all()
      serializer = CustomUserSerializer(users, many=True)
      return Response(serializer.data)
  
  def post(self, request):
      serializer = CustomUserSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()

          return Response(
              serializer.data,
              status=status.HTTP_201_CREATED
          )
      return Response(
          serializer.errors, 
          status=status.HTTP_400_BAD_REQUEST
          )
  
class CustomUserDetail(APIView):
  
  def get_object(self, pk):
      try:
          return CustomUser.objects.get(pk=pk)
      except CustomUser.DoesNotExist:
          raise Http404
      
  def get(self, request, pk):
      user = self.get_object(pk)
      serializer = CustomUserSerializer(user)
      return Response(serializer.data)
  
class CustomAuthToken(ObtainAuthToken):
   def post(self, request, *args, **kwargs):
       serializer = self.serializer_class(
           data=request.data,
           context={'request': request}
       )
       serializer.is_valid(raise_exception=True)
       user = serializer.validated_data['user']
       token, created = Token.objects.get_or_create(user=user)

       return Response({
           'token': token.key,
           'user_id': user.id,
           'email': user.email
       })
   


# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     An endpoint for changing password.
#     """
#     serializer_class = ChangePasswordSerializer
#     model = CustomUser
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["You gnome nothing John Snow - password is incorrect, try again"]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'The gnomes have accepted your new password and have hidden it in a secret garden pot',
#                 'data': []
#             }

#             return Response(response)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   




