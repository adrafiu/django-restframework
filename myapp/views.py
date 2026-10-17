from myapp.models import *
from myapp.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student_data = StudentModel.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        return Response({
            "success": True,
            "message": "Student data get sussessfully.",
            "data": serializer.data
        })
    if request.method == 'POST':
        serializer_data = StudentSerializer(data = request.data) 
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({
                "success": True,
                "message": "Student created successfully.",
                "data": serializer_data.data
            })
        return Response({
            "success": False,
            "message": "Invalid."
        })       