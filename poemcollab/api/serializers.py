from rest_framework import serializers
from api.models import Poem, PoemLine

class PoemLineSerializer(serializers.ModelSerializer):
	class Meta:
		model = PoemLine
		field = (
			'author', 
			'text',
		)

class PoemSerializer(serializers.ModelSerializer):
	lines = PoemLineSerializer(many=True)
	collaborators = serializers.Field()
	
	class Meta:
		model = Poem
		fields = (
			'owner',
			'lines',
			'collaborators',
		)
