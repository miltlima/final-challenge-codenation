from rest_framework.viewsets import ModelViewSet
from api.models import User

class UsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer