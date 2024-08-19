from rest_framework import serializers
from todoapi.models import Todo

# In case if we write a service that requires all fields of the Todo model class
class TodoAllDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = (
			"id", "title", "description",
		)
 
# In case if we write a service that requires only some fields of the Todo model class
class TodoSummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = (
			"id", "title",
		)