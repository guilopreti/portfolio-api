from rest_framework import generics
from utils.permissions import SuperUserPermission

from .models import BackEnd
from .serializers import AddTechSerializer, BackendSerializer, DeleteTechSerializer


# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = BackEnd.objects.all()
    serializer_class = BackendSerializer


class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [SuperUserPermission]

    queryset = BackEnd.objects.all()
    serializer_class = BackendSerializer


class RemoveTechView(generics.UpdateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = BackEnd.objects.all()
    serializer_class = DeleteTechSerializer


class AddTechView(generics.UpdateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = BackEnd.objects.all()
    serializer_class = AddTechSerializer
