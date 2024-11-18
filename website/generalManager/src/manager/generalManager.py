from __future__ import annotations
from typing import Type, Any
from generalManager.src.manager.meta import GeneralManagerMeta
from generalManager.src.interface import InterfaceBase
from generalManager.src.manager.bucket import Bucket


class GeneralManager(metaclass=GeneralManagerMeta):
    Interface: Type[InterfaceBase]

    def __init__(self, *args: Any, **kwargs: Any):
        self.__interface = self.Interface(*args, **kwargs)
        self.__id: dict[str, Any] = self.__interface.identification
        self.__attributes = self.__interface.getAttributes()
        self.__createAtPropertiesForAttributes()

    def __str__(self):
        return f"{self.__class__.__name__}({self.__id})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__id})"

    @property
    def id(self):
        return self.__id

    def __iter__(self):
        for key, value in self.__attributes.items():
            if callable(value):
                yield key, value()
                continue
            yield key, value

    def __createAtPropertiesForAttributes(self):

        def propertyMethod(attr_name: str) -> property:
            def getter(self: GeneralManager):
                attribute = self.__attributes[attr_name]
                if callable(attribute):
                    return attribute()
                return attribute

            return property(getter)

        for attr_name in self.__attributes.keys():
            setattr(self.__class__, attr_name, propertyMethod(attr_name))

    @classmethod
    def create(
        cls, creator_id: int, history_comment: str | None = None, **kwargs: Any
    ) -> GeneralManager:
        identification = cls.Interface.create(
            creator_id=creator_id, history_comment=history_comment, **kwargs
        )
        return cls(identification)

    def update(
        self, creator_id: int, history_comment: str | None = None, **kwargs: Any
    ) -> GeneralManager:
        self.__interface.update(
            creator_id=creator_id,
            history_comment=history_comment,
            **kwargs,
        )
        return self.__class__(self.__id)

    def deactivate(
        self, creator_id: int, history_comment: str | None = None
    ) -> GeneralManager:
        self.__interface.deactivate(
            creator_id=creator_id, history_comment=history_comment
        )
        return self.__class__(self.__id)

    @classmethod
    def filter(cls, **kwargs: Any) -> Bucket[GeneralManager]:
        return cls.Interface.filter(**kwargs)

    @classmethod
    def exclude(cls, **kwargs: Any) -> Bucket[GeneralManager]:
        return cls.Interface.exclude(**kwargs)

    @classmethod
    def all(cls) -> Bucket[GeneralManager]:
        return cls.Interface.filter()
