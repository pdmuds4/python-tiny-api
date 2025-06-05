from abc import ABC, abstractmethod

class ServiceModel(ABC):
    @abstractmethod
    def execute(self) -> any:
        pass