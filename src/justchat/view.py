# -*- coding: utf-8 -*-
from rest_framework import generics, permissions, status
from rest_framework.response import Response
#PicTime packages
from chat.models import Contact
# Third party packages
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'user',
            'image'
        )

class ContactDetails(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContactSerializer
    lookup_field = 'id'
