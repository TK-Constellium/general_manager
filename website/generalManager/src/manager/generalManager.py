from __future__ import annotations
from typing import Generic, Type, Any, TypeVar
from generalManager.src.manager.meta import GeneralManagerMeta
from generalManager.src.interface import InterfaceBase
from generalManager.src.manager.bucket import Bucket

T = TypeVar("T", bound="GeneralManager")


class GeneralManager(Generic[T], metaclass=GeneralManagerMeta):
    Interface: Type[InterfaceBase]
    _attributes: dict[str, Any]

    def __init__(self, *args: Any, **kwargs: Any):
        self._interface = self.Interface(*args, **kwargs)
        self.__id: dict[str, Any] = self._interface.identification

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
                yield key, value(self.__interface)
                continue
            yield key, value

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
    def filter(cls, **kwargs: Any) -> Bucket[T]:
        return cls.Interface.filter(**kwargs)

    @classmethod
    def exclude(cls, **kwargs: Any) -> Bucket[T]:
        return cls.Interface.exclude(**kwargs)

    @classmethod
    def all(cls) -> Bucket[T]:
        return cls.Interface.filter()
