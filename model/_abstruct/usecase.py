from .entity import EntityModel
from abc import ABC, abstractmethod

class UseCaseModel(ABC):
    @abstractmethod
    def execute(self) -> EntityModel:
        pass