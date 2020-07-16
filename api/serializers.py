from rest_framework.serializers import ModelSerializer
from api.models import User

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')

class LogEntrySerializer(serializers):
    class Meta:
        model = LogEntry
        fields = ('title', 'decription', 'createdAt', 'isArchived', 'colectedBy', 'category', 'level')
