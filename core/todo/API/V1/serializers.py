from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")

    class Meta:
        model = Task
        fields = ["id", "title", "user", "complete", "absolute_url"]
        read_only_fields = ["user"]
        
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("absolute_url", None)
        return rep
        
    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)
    
    def create(self, validated_data):
        validated_data["user"] = User.objects.get(id=self.context.get("request").user.id)
        return super().create(validated_data)
