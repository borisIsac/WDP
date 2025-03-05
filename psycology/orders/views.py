from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer
from .models import Order
from .permitions import IsNotAllowDeletePut



# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsNotAllowDeletePut]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    