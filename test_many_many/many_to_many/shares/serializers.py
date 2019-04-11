
from rest_framework import serializers
from shares.models import Share

class ShareLiteSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Share
        fields = ('id', 'name', 'selected')

    def get_selected(self, obj):
        return False

class ShareSerializer(serializers.ModelSerializer):
    function_name = serializers.CharField(allow_blank=True, default="")

    class Meta:
        model = Share
        fields = (
            'id', 'name', 'hostname', 'export_path','created_at','function_name',
        )

    def _get_instance_from_name(self, model, name):
        instance = None
        if not name:
            return instance
        try:
            instance = model.objects.get(name=name)
        except model.DoesNotExist:
            pass

        return instance

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return data

    def create(self, validated_data):
        share = Share.objects.create(**validated_data)
        return share