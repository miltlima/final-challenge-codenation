from rest_framework.viewsets import ModelViewSet
from api.models import User , LogEntry
from .serializers import UserSerializer, LogEntrySerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogEntryViewSet(ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer