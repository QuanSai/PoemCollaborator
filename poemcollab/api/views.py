from django.shortcuts import render

from api.models import Poem, PoemLine
from api.serializers import PoemSerializer, PoemLineSerializer

from rest_framework import generics


class PoemList(generics.ListCreateAPIView):
    """
	Get all Poems
    """

    queryset = Poem.objects.all()
    serializer_class = PoemSerializer

class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer

