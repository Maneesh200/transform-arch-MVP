import os
import re

from agents.base_agent import BaseAgent


class DependencyAnalyzerAgent(BaseAgent):

    def execute(self, context):

        repo_data = context.repository_analysis

        nodes = []
        edges = []

        all_classes = []

        for group in [

            repo_data["controllers"],
            repo_data["services"],
            repo_data["repositories"],
            repo_data["entities"]

        ]:

            all_classes.extend(group)

        class_names = {
            cls["name"]
            for cls in all_classes
        }

        # Build node list

        for cls in all_classes:

            nodes.append(cls["name"])

        # Find dependencies

        for cls in all_classes:

            current_class = cls["name"]

            file_path = cls["file"]

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                for class_name in class_names:

                    # Skip self dependency

                    if class_name == current_class:
                        continue

                    # Look for whole word match

                    pattern = rf"\b{re.escape(class_name)}\b"

                    if re.search(pattern, content):

                        edges.append({

                            "source": current_class,

                            "target": class_name

                        })

            except Exception as e:

                print(
                    f"Error reading {file_path}: {e}"
                )

        # Remove duplicate edges

        unique_edges = []

        seen = set()

        for edge in edges:

            key = (
                edge["source"],
                edge["target"]
            )

            if key not in seen:

                seen.add(key)

                unique_edges.append(edge)

        context.dependency_analysis = {

            "node_count": len(nodes),

            "edge_count": len(unique_edges),

            "coupling_score": len(unique_edges),

            "nodes": nodes,

            "edges": unique_edges

        }

        return context