from rest_framework import serializers

from postings.models import BlogPost

from django.contrib.auth import get_user_model

from django.db.models import Q



from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
User=get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
        def validate(self,data):
            email=data.get("email",None)
            username=data.get("username",None)
            password= data["password"]

            if not email and not username:
                raise ValidationError("A user or email is required to login.")
            user= User.objects.filter(
                Q(email=email)|
                Q(username=username)
            ).distinct()
            if user.exists() and user.count()==1:
                user_obj= user.first()
            else:
                raise ValidationError("This username/email is not valid")
            if user_obj:
                if not user_obj.check_password(password):
                    raise ValidationError("This username/password is not valid")
            data["token"]="abc"
            return data

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('pk',
                  'user',
                  'title',
                  'content',
                  'timestamp')
        read_only_fields = ['id', 'user']

def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)


def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value
