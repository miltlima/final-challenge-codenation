from rest_framework.serializers import ModelSerializer
from api.models import User, LogEntry

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'id')

class LogEntrySerializer(ModelSerializer):
    class Meta:
        model = LogEntry
        fields = ('id', 'title', 'description', 'createdAt', 'isArchived', 'colectedBy', 'category', 'level')
