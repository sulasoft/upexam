from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.db import IntegrityError

class UserListCreateAPIView(APIView):
    """
    API endpoint that allows users to be viewed or created.
    """

    def get(self, request, format=None):
        # Get all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileAPIView(APIView):
    """
    API endpoint that allows a single user to be viewed, updated, or deleted.
    """

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("User not found")

    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            try:
                serializer.save()

                # If email is updated, update the username as well
                if 'email' in request.data:
                    user.refresh_from_db()
                    user.save(update_fields=['username'])

                # Handle favorite profiles
                favorite_profiles = request.data.get('favorite_profiles', [])

                # Verify that the profile IDs exist
                existing_profiles = Profile.objects.filter(id__in=favorite_profiles)
                non_existing_profiles = set(favorite_profiles) - set(existing_profiles.values_list('id', flat=True))

                if non_existing_profiles:
                    return Response({"detail": f"Profiles with IDs {non_existing_profiles} do not exist."},
                                    status=status.HTTP_400_BAD_REQUEST)

                user.favorite_profiles.set(existing_profiles)

                return Response(serializer.data)

            except IntegrityError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileListCreateAPIView(APIView):
    """
    API endpoint that allows profiles to be viewed or created.
    """

    def get(self, request, format=None):
        # Get all profiles
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Create a new profile
        user_id = request.data.get('user')

        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                profile_data = {'user': user.id, 'name': request.data.get('name'), 'description': request.data.get('description')}
                
                serializer = ProfileSerializer(data=profile_data)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"detail": "User ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailAPIView(APIView):
    """
    API endpoint that allows a single profile to be viewed, updated, or deleted.
    """

    def get(self, request, pk, format=None):
        # Get profile by primary key
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # Update profile by primary key
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # Delete profile by primary key
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)