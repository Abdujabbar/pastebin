from .services import SharePasteService
from django.http import HttpResponse
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from .models import Paste
from .serializers import PasteSerializer

# Create your views here.
def index(request):
    return HttpResponse('Hello World')



class PasteRetriveAPIView(RetrieveAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer


class PasteCreateAPIView(CreateAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

    def post(self, request, *args, **kwargs):
        return SharePasteService().execute(**request.data)