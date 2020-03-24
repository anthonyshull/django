from rest_framework import mixins, viewsets

from .models import Engineer
from .serializers import EngineerSerializer


class EngineerViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
