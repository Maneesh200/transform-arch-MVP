from dataclasses import dataclass, field


@dataclass
class AnalysisContext:

    project_metadata: dict = field(default_factory=dict)

    architecture_detection: dict = field(default_factory=dict)

    repository_analysis: dict = field(default_factory=dict)

    dependency_analysis: dict = field(default_factory=dict)

    domain_analysis: dict = field(default_factory=dict)

    recommendations: dict = field(default_factory=dict)

    report: dict = field(default_factory=dict)