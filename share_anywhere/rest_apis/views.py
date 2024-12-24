from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Command
from .serializers import CommandSerializer

class CommandListCreateView(APIView):
    def get(self, request):
        commands = Command.objects.all()
        serializer = CommandSerializer(commands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommandDetailView(APIView):
    def get(self, request, pk):
        try:
            command = Command.objects.get(pk=pk)
        except Command.DoesNotExist:
            return Response({'error': 'Command not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommandSerializer(command)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            command = Command.objects.get(pk=pk)
        except Command.DoesNotExist:
            return Response({'error': 'Command not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommandSerializer(command, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            command = Command.objects.get(pk=pk)
            command.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Command.DoesNotExist:
            return Response({'error': 'Command not found'}, status=status.HTTP_404_NOT_FOUND)

