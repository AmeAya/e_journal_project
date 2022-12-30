from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from e_journal_app.models import Student
from .serializers import StudentSerializer

class StudentApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        thisStudent = Student.objects.get(user_id=request.user)
        serializer = StudentSerializer(thisStudent, many=False)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        data = {
            'surname': request.data.get('surname'),
            'name': request.data.get('name'),
            'group': request.data.get('group')
        }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
