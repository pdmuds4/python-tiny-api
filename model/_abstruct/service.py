from .entity import EntityModel
from .repository import RepositoryModel
from abc import ABC, abstractmethod

class ServiceModel(ABC):
    def __init__(self, repository: RepositoryModel, request: EntityModel):
        self.repository = repository
        self.request = request

    @abstractmethod
    def execute(self) -> EntityModel:
        pass