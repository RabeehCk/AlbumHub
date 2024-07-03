from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import authentication,permissions

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.decorators import action

from api.serializers import AlbumSerializer,TrackSerializer,RegistrationSerializer,ReviewSerializer

from api.models import Album,Tracks,Review

from api.permissions import OwnerOnly


class UserRegisterView(APIView):

    def post(self,request,*args,**kwargs):

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class AlbumViewsetView(ModelViewSet):

    serializer_class = AlbumSerializer

    queryset = Album.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]


    @action(methods=["post"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id =kwargs.get("pk")

        album_instance = Album.objects.get(id=id)

        serializer = TrackSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        

class TrackViewSetView(RetrieveUpdateDestroyAPIView):

    serializer_class = TrackSerializer

    queryset = Tracks.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]


class ReviewViewsetView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [OwnerOnly]

    def post(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        album_instance = Album.objects.get(id=id)

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user,album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)


class ReviewMixinView(RetrieveUpdateDestroyAPIView):

    serializer_class = ReviewSerializer

    queryset = Review.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [OwnerOnly]