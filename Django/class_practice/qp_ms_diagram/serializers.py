from rest_framework import serializers
from .models import Question, MarkScheme, diagram


class DiagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = diagram
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    diagrams = DiagramSerializer(many = True, read_only = False)
    class Meta:
        model = Question
        fields = ['id', 'text', 'embeddings', 'diagrams']

    def create(self, validated_data):
        diagram_data = validated_data.pop('diagrams', [])
        question = Question.objects.create(**validated_data)
        if diagram_data:
            for diagram_object in diagram_data:
                diagram.objects.create(question = question, **diagram_object)

        return question
        
class MarkSchemeSerializer(serializers.ModelSerializer):
    diagrams = DiagramSerializer(many = True, read_only = False)
    class Meta:
        model = MarkScheme
        fields = ['id', 'text', 'diagrams']

    def create(self, validated_data):
        diagram_list = validated_data.pop('diagrams', [])
        mark_scheme = MarkScheme.objects.create(**validated_data)
        if diagram_list:
            for diagram_object in diagram_list:
                diagram.objects.create(mark_scheme = mark_scheme, **diagram_object)

        return mark_scheme