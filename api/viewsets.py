from rest_framework.viewsets import ModelViewSet
from api.models import User , LogEntry
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, LogEntrySerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class LogEntryViewSet(ModelViewSet):
    serializer_class = LogEntrySerializer
    def get_queryset(self):
        return LogEntry.objects.filter(isArchived=False)