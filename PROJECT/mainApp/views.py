from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Topic, Audio
from .serializers import TopicSerializer, AudioSerializer

from drf_yasg.utils import swagger_auto_schema


class TopicsAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Get all topics",
        responses={200: AudioSerializer()}
    )
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)


class AudiosAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Get all audios",
        responses={200: AudioSerializer()}
    )
    def get(self, request):
        audios = Audio.objects.all()
        serializer = AudioSerializer(audios, many=True)
        return Response(serializer.data)


# class AudioAPIView(APIView):
#     @swagger_auto_schema(
#         operation_description="Get audio by ID",
#         responses={200: AudioSerializer()}
#     )
#     def get(self, request, pk):
#         audio = Audio.objects.get(id=pk)
#         serializer = AudioSerializer(audio)
#         return Response(serializer.data)

class AudiosByTopicAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Get audios by topic",
        responses={200: AudioSerializer()}
    )
    def get(self, request, pk):
        audios = Audio.objects.filter(topic__id=pk)
        serializer = AudioSerializer(audios, many=True)
        return Response(serializer.data)