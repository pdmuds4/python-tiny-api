from abc import ABC, abstractmethod

class ServiceModel(ABC):
    def __init__(self, client: any, request: any):
        self.client = client
        self.request = request

    @abstractmethod
    def execute(self) -> any:
        pass