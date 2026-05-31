from dataclasses import dataclass

@dataclass
class ProjectMetadata:
    project_name: str
    project_path: str
    language: str
    framework: str
    build_tool: str
    total_files: int
    java_files: int