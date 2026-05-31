import streamlit as st

from scanners.project_extractor import extract_project
from scanners.java_scanner import scan_project

from models.analysis_context import AnalysisContext

from orchestrator.agent_orchestrator \
    import AgentOrchestrator


st.title("ArchTransform AI")


uploaded_file = st.file_uploader(
    "Upload Spring Boot Project ZIP",
    type=["zip"]
)

if uploaded_file:

    project_path = extract_project(uploaded_file)

    scan_result = scan_project(project_path)

    context = AnalysisContext()

    context.project_metadata = {

        "project_name": uploaded_file.name,

        "project_path": project_path,

        **scan_result
    }

    orchestrator = AgentOrchestrator()

    context = orchestrator.run(context)

    st.subheader("Project Metadata")

    st.json(context.project_metadata)

    st.subheader("Architecture Detection")

    st.json(context.architecture_detection)

    st.subheader("Repository Analysis")

    st.json(context.repository_analysis)

    st.subheader("Dependency Analysis")

    st.json(context.dependency_analysis)

    st.subheader("Domain Analysis")

    st.json(context.domain_analysis)