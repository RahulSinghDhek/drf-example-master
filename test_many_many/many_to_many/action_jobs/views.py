from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from action_jobs.serializers import ActionJobSerializer
from action_jobs.models import ActionJob
from rest_framework import status as status_codes
from rest_framework.response import Response

class ViewSetList(ListCreateAPIView):
    queryset = ActionJob.objects.all()
    serializer_class = ActionJobSerializer


class ViewSetCRUD(RetrieveUpdateDestroyAPIView):
    queryset = ActionJob.objects.all()
    serializer_class = ActionJobSerializer


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        job = self.get_object()
        serializer = self.get_serializer(job, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(status_codes.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        job = self.get_object()

        job.delete()
        return Response(status=status_codes.HTTP_204_NO_CONTENT)
