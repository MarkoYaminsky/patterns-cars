from rest_framework import serializers


class BaseStringOutputSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            key: value if isinstance(value, bool) else str(value)
            for key, value in representation.items()
        }
