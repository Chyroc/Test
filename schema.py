# -*- coding: utf-8 -*-

from graphene_sqlalchemy import SQLAlchemyObjectType
from models import People as PeopleModel
from models import Degrees as DegreesModel
import graphene


class People(SQLAlchemyObjectType):
    class Meta:
        model = PeopleModel


class Degrees(SQLAlchemyObjectType):
    class Meta:
        model = DegreesModel


class Query(graphene.ObjectType):
    peoples = graphene.List(People)
    degreess = graphene.List(Degrees)

    def resolve_peoples(self, args, context, info):
        query = People.get_query(context)
        return query.all()

    def resolve_degreess(self, args, context, info):
        query = Degrees.get_query(context)
        return query.all()


schema = graphene.Schema(query=Query)
