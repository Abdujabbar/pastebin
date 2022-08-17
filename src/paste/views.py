from .services import SharePasteService
from django.http import HttpResponse
from rest_framework.generics import RetrieveAPIView, CreateAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Paste
from .serializers import PasteSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,) 

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class PasteRetriveAPIView(RetrieveAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer


class PasteCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

    def post(self, request, *args, **kwargs):
        return SharePasteService().execute(**request.data)