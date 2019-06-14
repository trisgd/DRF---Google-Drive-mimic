from postings.models import BlogPost
from rest_framework import generics,mixins
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )




class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
#@login_required
class BlogPostAPIView(mixins.CreateModelMixin,generics.ListAPIView): # DetailView CreateView FormView
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    # permission_classes      = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return BlogPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}
#@login_required
class BlogPost_non_createView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}
