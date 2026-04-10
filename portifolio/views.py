from rest_framework.response import Response
from rest_framework.views import APIView

from frontend.models import FrontEnd
from backend.models import BackEnd
from fullstack.models import FullStack

from frontend.serializers import FrontendSerializer
from backend.serializers import BackendSerializer
from fullstack.serializers import FullstackSerializer


class AllProjectsByDateView(APIView):
    """
    View que traz todos os projetos agrupados (Frontend, Backend e Fullstack),
    ordenados pela data de registro (do mais recente para o mais antigo).
    """

    def get(self, request):
        front_queryset = FrontEnd.objects.all()
        back_queryset = BackEnd.objects.all()
        full_queryset = FullStack.objects.all()

        front_data = FrontendSerializer(front_queryset, many=True).data
        back_data = BackendSerializer(back_queryset, many=True).data
        full_data = FullstackSerializer(full_queryset, many=True).data

        all_projects = front_data + back_data + full_data

        all_projects.sort(key=lambda x: x.get("registration_date", ""), reverse=True)

        return Response(all_projects)
