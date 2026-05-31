import os

def scan_project(project_path):

    total_files = 0
    java_files = 0

    framework = "Unknown"
    build_tool = "Unknown"

    for root, dirs, files in os.walk(project_path):

        for file in files:

            total_files += 1

            if file.endswith(".java"):
                java_files += 1

            if file == "pom.xml":
                build_tool = "Maven"

            if file == "build.gradle":
                build_tool = "Gradle"

    return {
        "total_files": total_files,
        "java_files": java_files,
        "framework": framework,
        "build_tool": build_tool
    }