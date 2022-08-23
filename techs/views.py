from rest_framework import generics

from techs.models import Technology
from techs.permissions import SuperUserPermission

from .serializers import TechSerializer


# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = Technology.objects.all()
    serializer_class = TechSerializer


class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [SuperUserPermission]

    queryset = Technology.objects.all()
    serializer_class = TechSerializer
