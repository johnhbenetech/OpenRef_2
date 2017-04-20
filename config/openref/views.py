from django.http import HttpResponse
from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Provider, ProviderUpdate
from .serializers import ProviderSerializer, ProviderUpdateSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
 
 
class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'provider_id'
	
    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user)

class ProviderDetail(generics.RetrieveUpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'provider_id'

class ProviderUpdateList(generics.ListCreateAPIView):
    serializer_class = ProviderUpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_url_kwarg = 'provider_id'

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            provider_id=self.kwargs['provider_id'])
			
    def get_queryset(self):
        provider = self.kwargs['provider_id']
        return ProviderUpdate.objects.filter(provider__id=provider)
			
class ProviderUpdateDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProviderUpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'providerupdate_id'
 
    def get_queryset(self):
        providerupdate = self.kwargs['providerupdate_id']
        return ProviderUpdate.objects.filter(id=providerupdate)
