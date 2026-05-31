import os

from agents.base_agent import BaseAgent


class RepositoryAnalyzerAgent(BaseAgent):

    def execute(self, context):

        project_path = context.project_metadata["project_path"]

        controllers = []
        services = []
        repositories = []
        entities = []

        for root, dirs, files in os.walk(project_path):

            for file in files:

                if not file.endswith(".java"):
                    continue

                full_path = os.path.join(root, file)

                try:

                    with open(
                        full_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                        class_info = {
                            "name": file.replace(".java", ""),
                            "file": full_path
                        }

                        if "@RestController" in content \
                                or "@Controller" in content:

                            controllers.append(class_info)

                        if "@Service" in content:

                            services.append(class_info)

                        if "@Repository" in content \
                                or "JpaRepository" in content:

                            repositories.append(class_info)

                        if "@Entity" in content:

                            entities.append(class_info)

                except Exception:
                    pass

        context.repository_analysis = {

        "controller_count": len(controllers),

        "service_count": len(services),

        "repository_count": len(repositories),

        "entity_count": len(entities),

        "controllers": controllers,

        "services": services,

        "repositories": repositories,

        "entities": entities
    }

        return context