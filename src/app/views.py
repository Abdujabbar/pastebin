from django.urls import reverse

from .models import Paste

from .forms import PasteForm
from .services import SharePasteService
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework.response import Response
from django.views import View
from .serializers import PasteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication


class PasteView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'paste/form.html'
    
    def get(self, request):
        form = PasteForm()

        return render(request, self.template_name, {'formset': form})

    def post(self, request):
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = SharePasteService().execute(
                    form.data.get('expired_at'), 
                    form.data.get('content'), 
                    request.user)
            
            return redirect('paste_detail', short_url=paste.short_url)
        
        
        return render(request, self.template_name, {'formset': form})


class PasteRendererView(View):
    template_name = 'paste/show.html'
    def get(self, request, short_url):
        paste = get_object_or_404(Paste, short_url=short_url)
        
        return render(request, self.template_name, {'paste': paste})


# class PasteCreateAPIView(CreateAPIView):
#     permission_classes = (IsAuthenticated,) 
#     authentication_classes = (SessionAuthentication, JWTAuthentication,) 
#     queryset = Paste.objects.all()
#     serializer_class = PasteSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.instance = SharePasteService().execute(
#             request.data.get('expired_at'), 
#             request.data.get('content'), 
#             request.user)
        
#         return Response(
#             status=201,
#             data = {
#                 'short_url': request.get_host() + reverse('paste_detail', kwargs={'short_url':serializer.data.get('short_url')})
#             }
#         )
