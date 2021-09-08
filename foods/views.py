from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Food
from .permissions import IsOwnerOrReadOnly
from .serializers import FoodSerializer


class FoodList(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
