from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from e_journal_app.models import Student, Group
from .serializers import StudentSerializer, GroupSerializer

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

class GroupDetailApiView(APIView):
    def get_object(self, group_id):
        try:
            return Group.objects.get(id=group_id)
        except:
            return None

    def get(self, request, group_id, *args, **kwargs):
        thisGroup = self.get_object(group_id)
        if thisGroup is None:
            return Response(
                data={'error': 'Group does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            serializer = GroupSerializer(thisGroup)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

    def put(self, request, group_id, *args, **kwargs): # update
        thisGroup = self.get_object(group_id)
        if thisGroup is None:
            return Response(
                data={'error': 'Group does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            data = {
                'name': request.data.get('name'),
                'admission_year': request.data.get('admission_year')
            }
            serializer = GroupSerializer(
                instance=thisGroup,
                data=data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
