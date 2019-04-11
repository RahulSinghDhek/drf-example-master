from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from shares.models import Share
from shares.serializers import ShareLiteSerializer, ShareSerializer
from rest_framework import status as status_codes
from rest_framework.response import Response

class ShareList(ListCreateAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer



class ShareRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete share.
    """
    queryset = Share.objects.all()
    serializer_class = ShareSerializer


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        share = self.get_object()
        serializer = self.get_serializer(
            share, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(status_codes.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        share = self.get_object()

        share.delete()
        return Response(status=status_codes.HTTP_204_NO_CONTENT)

