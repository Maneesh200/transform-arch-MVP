from agents.architecture_detection_agent import ArchitectureDetectionAgent
from agents.repository_analyzer_agent import RepositoryAnalyzerAgent
from agents.dependency_analyzer_agent import DependencyAnalyzerAgent
from agents.domain_discovery_agent import DomainDiscoveryAgent
from agents.recommendation_agent import RecommendationAgent


class AgentOrchestrator:

    def __init__(self):

        self.agents = [
            
            ArchitectureDetectionAgent(),

            RepositoryAnalyzerAgent(),

            DependencyAnalyzerAgent(),
            
            DomainDiscoveryAgent(),
            
            RecommendationAgent()

        ]

    def run(self, context):

        for agent in self.agents:

            context = agent.execute(context)

        return context