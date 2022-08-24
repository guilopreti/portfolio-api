from rest_framework import generics
from utils.permissions import SuperUserPermission

from .models import BackEnd
from .serializers import BackendSerializer


# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = BackEnd.objects.all()
    serializer_class = BackendSerializer
