from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
import graphene
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class LoggedInUserType(DjangoObjectType):
    class Meta:
        model = User 
        fields = ['id', 'username']

class AuthPayload(graphene.ObjectType):
    user = graphene.Field(LoggedInUserType)

    def resolve_user(self, info):
        # Resolve the user field here if needed
        return self.user

class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
    
    auth_payload = graphene.Field(AuthPayload)
    
    @staticmethod
    def mutate(root, info, username, password):
        if user := authenticate(info.context, username=username, password=password):
            login(info.context, user)
            return Login(auth_payload=AuthPayload(user=user))
        raise GraphQLError("Authentication Failed, Please check your credentials!")
