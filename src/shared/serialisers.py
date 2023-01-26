from rest_framework import serializers


class ResponseSerialiser(serializers.Serializer):
    result = serializers.DictField()


class ResponseMultiSerialiser(serializers.Serializer):
    result = serializers.ListField()