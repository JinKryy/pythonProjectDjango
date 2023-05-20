import graphene

import shorty.schema

class Query(shorty.schema.Query, graphene.ObjectType):
    pass

class Mutation(shorty.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)