from rest_framework import generics
from utils.permissions import SuperUserPermission

from .models import FullStack
from .serializers import FullstackSerializer


# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FullStack.objects.all()
    serializer_class = FullstackSerializer
