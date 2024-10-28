from django.apps import AppConfig
import graphene


class GeneralmanagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "generalManager"

    def ready(self):
        # Importieren Sie die Metaklasse
        from generalManager.src.manager.meta import GeneralManagerMeta

        # Erstellen der GraphQL-Interfaces
        for general_manager_class in GeneralManagerMeta.pending_graphql_interfaces:
            GeneralManagerMeta._createGraphQlInterface(general_manager_class)

        # Erstellen der Query-Klasse
        query_class = type(
            "Query", (graphene.ObjectType,), GeneralManagerMeta._query_fields
        )
        GeneralManagerMeta._query_class = query_class

        # Schema erstellen
        from . import schema

        schema.schema = graphene.Schema(query=GeneralManagerMeta._query_class)
