from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from JobApp.models import JobDb,ApplicationDb
from JobApp.serializers import JobSerializer,ApplicationSerializer

# Create your views here.
class JobView(APIView):
    def get(self,request):
        qs = JobDb.objects.all()
        serializer_instance = JobSerializer(qs, many=True)
        return Response(data = serializer_instance.data) 

    def post(self,request):
        form_data = request.data
        serializer_instance = JobSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            JobDb.objects.create(**actual_data)
            return Response({"Message":"Job Created Successfully"})
        else:
            return Response(data=serializer_instance.errors)

class JobRetriveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs = JobDb.objects.get(id=pk)
        serializer_instance = JobSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data = request.data
        serializer_instance = JobSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            JobDb.objects.filter(id=pk).update(**actual_data)
            return Response({"Message":"Job Updated Successfully"})
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        qs = JobDb.objects.filter(id=pk).delete()
        serializer_insatnce = JobSerializer(qs)
        return Response({"Message":"Job Deleted Successfully"})

class ApplicationView(APIView):
    def get(self,request):
        qs = ApplicationDb.objects.all()
        serializer_instance = ApplicationSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = ApplicationSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            ApplicationDb.objects.create(**actual_data)
            return Response({"Message":"Application Submitted Successfully"})
        else:
            return Response(data=serializer_instance.errors)
    
class ApplicationRetriveUpdateDelete(APIView):
    def get(self,request,pk):
        qs = ApplicationDb.objects.get(id=pk)
        serializer_instance = ApplicationSerializer(qs)
        return Response(data=serializer_instance.data)
    
    def put(self,request,pk):
        form_data = request.data
        serializer_instance = ApplicationSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            ApplicationDb.objects.filter(id=pk).update(**actual_data)
            return Response({"Message":"Application Upadted Successfully"})
        else:
            return Response(data=serializer_instance.errors)
        
    def delete(self,request,pk):
        qs = ApplicationDb.objects.filter(id=pk).delete()
        serializer_insatnce = ApplicationSerializer(qs)
        return Response({"Message":"Application Deleted Successfully"})

class EvaluateApplicationView(APIView):
    def put(self,request,pk):
        form_data = request.data
        ApplicationDb.objects.filter(id=pk).update(**form_data)
        return Response({"Message":"Application Updated"})