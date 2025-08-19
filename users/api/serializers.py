from users.models import Profile
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField
from rest_framework.serializers import EmailField


class ProfileSerializer(ModelSerializer):
    username = CharField(source='user.username', required=False)
    email = EmailField(source='user.email', required=True)
    first_name = CharField(source='user.first_name', required=True)
    second_name = CharField(source='user.second_name', required=False, allow_null=True)
    last_name = CharField(source='user.last_name', required=True)
    second_last_name = CharField(source='user.second_last_name', required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'email',
            'avatar',
            'bio',
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})

        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
