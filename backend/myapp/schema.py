import graphene
from .views import Login, GoogleLogin

class Query(graphene.ObjectType):
    hello = graphene.String()
    
    def resolve_hello(self, info):
        return "Hello GraphQL"
    
class Mutation(graphene.ObjectType):
    login = Login.Field()
    googleLogin = GoogleLogin.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
