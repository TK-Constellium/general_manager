from django.apps import AppConfig
import graphene
from django.conf import settings
from django.urls import path
from graphene_django.views import GraphQLView
from importlib import import_module


class GeneralmanagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "generalManager"

    def ready(self):
        from generalManager.src.manager.meta import GeneralManagerMeta
        from generalManager.src.manager.generalManager import GeneralManager
        from generalManager.src.manager.input import Input
        from generalManager.src.api.property import graphQlProperty

        for general_manager_class in GeneralManagerMeta.all_classes:
            attributes = getattr(general_manager_class.Interface, "input_fields", {})
            for attribute_name, attribute in attributes.items():
                if isinstance(attribute, Input) and issubclass(
                    attribute.type, GeneralManager
                ):
                    connected_manager = attribute.type
                    func = lambda x, attribute_name=attribute_name: general_manager_class.filter(
                        **{attribute_name: x}
                    )

                    func.__annotations__ = {"return": general_manager_class}
                    setattr(
                        connected_manager,
                        f"{general_manager_class.__name__.lower()}_list",
                        graphQlProperty(func),
                    )

        for (
            general_manager_class
        ) in GeneralManagerMeta.pending_attribute_initialization:
            attributes = general_manager_class.Interface.getAttributes()
            setattr(general_manager_class, "_attributes", attributes)
            GeneralManagerMeta.createAtPropertiesForAttributes(
                attributes, general_manager_class
            )

        if getattr(settings, "AUTOCREATE_GRAPHQL", False):
            from generalManager.src.api.graphql import GraphQL

            for general_manager_class in GeneralManagerMeta.pending_graphql_interfaces:
                GraphQL.createGraphqlInterface(general_manager_class)

            query_class = type("Query", (graphene.ObjectType,), GraphQL._query_fields)
            GraphQL._query_class = query_class

            schema = graphene.Schema(query=GraphQL._query_class)
            self.add_graphql_url(schema)

    def add_graphql_url(self, schema):
        root_url_conf_path = getattr(settings, "ROOT_URLCONF", None)
        graph_ql_url = getattr(settings, "GRAPHQL_URL", "graphql/")
        if not root_url_conf_path:
            raise Exception("ROOT_URLCONF not found in settings")
        urlconf = import_module(root_url_conf_path)
        urlconf.urlpatterns.append(
            path(
                graph_ql_url,
                GraphQLView.as_view(graphiql=True, schema=schema),
            )
        )
