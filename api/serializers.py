from rest_framework.serializers import ModelSerializer
from api.models import User

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')
