from rest_framework.viewsets import ModelViewSet
from api.models import User , LogEntry
from .serializers import UserSerializer, LogEntrySerializer

class UsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogEntryView(ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer