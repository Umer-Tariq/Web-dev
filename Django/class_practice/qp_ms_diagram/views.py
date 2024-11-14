from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import QuestionSerializer, MarkSchemeSerializer
from .models import Question, MarkScheme
from rest_framework.response import Response


class QuestionManager(GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        questions = self.get_queryset()
        serializer = self.get_serializer(questions, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'question created successfully'})
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id, *args, **kwargs):
        question = self.get_object()
        question.delete()
        return Response({"message" : "question deleted successfully"})

class MarkSchemeManager(GenericAPIView):
    queryset = MarkScheme.objects.all()
    serializer_class = MarkSchemeSerializer

    def get(self, request, *args, **kwargs):
        mark_schemes = self.get_queryset()
        serializer = self.get_serializer(mark_schemes, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = self.get_serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Mark scheme created successfully'})
        else:
            return Response({serializer.errors})