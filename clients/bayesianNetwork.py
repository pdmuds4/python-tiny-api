from pgmpy.models import DiscreteBayesianNetwork

class BayesianNetworkClient(DiscreteBayesianNetwork):
    def __init__(self, ebunch: list):
        super().__init__(ebunch)

