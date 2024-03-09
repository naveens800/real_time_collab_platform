from graphene_django.types import DjangoObjectType
import graphene

class LoggedInUserType(DjangoObjectType):
    class Meta:
        model = User 
        fields = ['id', 'username']


class AuthPayload(graphene.ObjectType):
    user = graphene.Field(LoggedInUserType)

    def resolve_user(self, info):
        # Resolve the user field here if needed
        return self.user


class UserType(DjangoObjectType):
    class Meta:
        model = User