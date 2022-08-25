from rest_framework import generics
from utils.permissions import SuperUserPermission

from .models import FrontEnd
from .serializers import AddTechSerializer, DeleteTechSerializer, FrontendSerializer


# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FrontEnd.objects.all()
    serializer_class = FrontendSerializer


class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FrontEnd.objects.all()
    serializer_class = FrontendSerializer


class RemoveTechView(generics.UpdateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FrontEnd.objects.all()
    serializer_class = DeleteTechSerializer


class AddTechView(generics.UpdateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FrontEnd.objects.all()
    serializer_class = AddTechSerializer
