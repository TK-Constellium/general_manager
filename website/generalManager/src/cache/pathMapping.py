from __future__ import annotations
from typing import TYPE_CHECKING, cast, get_args
from generalManager.src.manager.meta import GeneralManagerMeta
from generalManager.src.manager.generalManager import GeneralManager
from generalManager.src.api.property import GraphQLProperty
from generalManager.src.interface.baseInterface import Bucket


type PathStart = str
type PathDestination = str


class PathMap:

    instance: PathMap
    mapping: dict[tuple[PathStart, PathDestination], PathTracer] = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
            cls.createPathMapping()
        return cls.instance

    @classmethod
    def createPathMapping(cls):
        all_managed_classes = GeneralManagerMeta.all_classes
        for start_class in all_managed_classes:
            for destination_class in all_managed_classes:
                if start_class != destination_class:
                    cls.instance.mapping[
                        (start_class.__name__, destination_class.__name__)
                    ] = PathTracer(start_class, destination_class)

    def __init__(self, path_start: PathStart | GeneralManager | type[GeneralManager]):

        if isinstance(path_start, GeneralManager):
            self.start_instance = path_start
            self.start_class = path_start.__class__
            self.start_class_name = path_start.__class__.__name__
        elif isinstance(path_start, type):
            self.start_instance = None
            self.start_class = path_start
            self.start_class_name = path_start.__name__
        else:
            self.start_instance = None
            self.start_class = None
            self.start_class_name = path_start

    def to(
        self, path_destination: PathDestination | type[GeneralManager] | str
    ) -> PathTracer | None:
        if isinstance(path_destination, type):
            path_destination = path_destination.__name__

        tracer = self.mapping.get((self.start_class_name, path_destination), None)
        if not tracer:
            return None
        return tracer

    def goTo(
        self, path_destination: PathDestination | type[GeneralManager] | str
    ) -> GeneralManager | Bucket | None:
        if isinstance(path_destination, type):
            path_destination = path_destination.__name__

        tracer = self.mapping.get((self.start_class_name, path_destination), None)
        if not tracer:
            return None
        if not self.start_instance:
            raise ValueError("Cannot call goTo on a PathMap without a start instance.")
        return tracer.traversePath(self.start_instance)


class PathTracer:
    def __init__(
        self, start_class: type[GeneralManager], destination_class: type[GeneralManager]
    ):
        self.start_class = start_class
        self.destination_class = destination_class
        if self.start_class == self.destination_class:
            self.path = []
        else:
            self.path = self.createPath(start_class, [])

    def createPath(
        self, current_manager: type[GeneralManager], path: list[str]
    ) -> list[str] | None:
        current_connections = current_manager.Interface.getAttributeTypes()
        for attr_name, attr_value in current_manager.__dict__.items():
            if not isinstance(attr_value, GraphQLProperty):
                continue
            type_hints = get_args(attr_value.graphql_type_hint)
            field_type = (
                type_hints[0]
                if type_hints
                else cast(type, attr_value.graphql_type_hint)
            )
            current_connections[attr_name] = field_type
        for attr, attr_type in current_connections.items():
            if attr in path or attr_type == self.start_class:
                continue
            if not issubclass(attr_type, GeneralManager):
                continue
            if attr_type == self.destination_class:
                return [*path, attr]
            result = self.createPath(attr_type, [*path, attr])
            if result:
                return result

        return None

    def traversePath(
        self, start_instance: GeneralManager | Bucket
    ) -> GeneralManager | Bucket | None:
        current_instance = start_instance
        if not self.path:
            return None
        for attr in self.path:
            if not isinstance(current_instance, Bucket):
                current_instance = getattr(current_instance, attr)
                continue
            new_instance = None
            for entry in current_instance:
                if not new_instance:
                    new_instance = getattr(entry, attr)
                else:
                    new_instance = new_instance | getattr(entry, attr)
            current_instance = new_instance

        return current_instance
