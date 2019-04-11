
from rest_framework import serializers
from action_jobs.models import ActionJob
from shares.models import  Share


class ActionJobSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=False)
    shares = serializers.StringRelatedField(many=True, required=False)


    class Meta:
        model = ActionJob
        fields = (
            'id', 'name', 'comments','created_at','shares',
        )
    def to_internal_value(self, data):
        shares = data.pop('shares', [])
        if shares and not isinstance(shares, list):
            raise serializers.ValidationError({
                'shares': ("This field should be a list of share names.")
            })

        shares = Share.objects.filter(id__in=shares)
        if not shares:
            raise serializers.ValidationError({
                'shares': ("At least one share should be selected.")
            })

        data = super().to_internal_value(data)
        data.update({
            'shares': shares,
        })
        return data

    def validate_name(self, name):
        if self.instance and self.instance.name == name:
            return name

        if ActionJob.objects.filter(name=name).exists():
            err = (" Job with this name already exists.")
            raise serializers.ValidationError(err)

        return name

    def create(self, validated_data):
        shares = validated_data.pop('shares')
        job = ActionJob.objects.create(**validated_data)
        job.set_shares(*shares)
        job_data = {
            "actionjob_id": job.id,
            "share_ids": [share.id for share in shares]
        }
        return job

    def update(self, instance, validated_data):
        shares = validated_data.pop('shares')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.set_shares(*shares)
        job_data = {
            "actionjob_id": instance.id,
            "share_ids": [share.id for share in shares]
        }
        instance.save()

        return instance


