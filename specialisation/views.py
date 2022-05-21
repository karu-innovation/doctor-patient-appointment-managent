from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .serialization import specialisationSerializer
from .models import Specialisation
from rest_framework.response import Response

# Create your views here.


# specialisation viewset
# api view
@api_view(['GET', 'POST'])
def specialisation_view(request):
    if request.method == 'GET':
        serializer = specialisationSerializer(Specialisation, many=True)
        return Response(serializer.data)
    
    return render(request, 'specialisation/specialisation.html')

@api_view(['GET','PUT', 'DELETE'])
def specialisation_detail(request, uuid):
    try:
        specialty = Specialisation.objects.get(uuid=uuid)
    except:
         return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = specialisationSerializer(specialty)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = specialisationSerializer(specialty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        specialty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


