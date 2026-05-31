import os

from agents.base_agent import BaseAgent


class ArchitectureDetectionAgent(BaseAgent):

    def execute(self, context):

        project_path = context.project_metadata["project_path"]

        evidence = []

        spring_boot_found = False

        for root, dirs, files in os.walk(project_path):

            for file in files:

                full_path = os.path.join(root, file)

                try:

                    if file.endswith(".java"):

                        with open(full_path, "r", encoding="utf-8") as f:

                            content = f.read()

                            if "@SpringBootApplication" in content:

                                spring_boot_found = True
                                evidence.append("@SpringBootApplication")

                    elif file == "pom.xml":

                        with open(full_path, "r", encoding="utf-8") as f:

                            content = f.read()

                            if "spring-boot-starter" in content:

                                spring_boot_found = True
                                evidence.append("spring-boot-starter")

                    elif file == "build.gradle":

                        with open(full_path, "r", encoding="utf-8") as f:

                            content = f.read()

                            if "org.springframework.boot" in content:

                                spring_boot_found = True
                                evidence.append("org.springframework.boot")

                except Exception:
                    pass

        context.architecture_detection = {

            "framework": "Spring Boot"
            if spring_boot_found
            else "Unknown",

            "architecture_type": "Layered Monolith",

            "confidence": 95
            if spring_boot_found
            else 40,

            "evidence": list(set(evidence))
        }

        return context