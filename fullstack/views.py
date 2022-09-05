from rest_framework import generics
from utils.permissions import SuperUserPermission

from .models import FullStack
from .serializers import AddTechsSerializer, DeleteTechsSerializer, FullstackSerializer


# Create your views here.
class ListCreateView(generics.ListCreateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FullStack.objects.all()
    serializer_class = FullstackSerializer


class ListByDateView(generics.ListAPIView):

    queryset = FullStack.objects.all()
    serializer_class = FullstackSerializer

    def get_queryset(self):

        return self.queryset.order_by("-registration_date")


class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FullStack.objects.all()
    serializer_class = FullstackSerializer


class RemoveTechView(generics.UpdateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FullStack.objects.all()
    serializer_class = DeleteTechsSerializer


class AddTechView(generics.UpdateAPIView):
    permission_classes = [SuperUserPermission]

    queryset = FullStack.objects.all()
    serializer_class = AddTechsSerializer
