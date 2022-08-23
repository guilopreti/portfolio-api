from rest_framework import generics
from utils.permissions import SuperUserPermission

from .models import FrontEnd
from .serializers import FrontendSerializer


# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FrontEnd.objects.all()
    serializer_class = FrontendSerializer
