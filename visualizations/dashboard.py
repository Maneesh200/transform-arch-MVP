import streamlit as st


def render_dashboard(context):
    st.error("This dashboard is a work in progress. Please check back later for updates.")
    architecture = context.architecture_detection
    repo = context.repository_analysis
    dependency = context.dependency_analysis
    domains = context.domain_analysis
    recommendations = context.recommendations

    st.title("🚀 ArchTransform AI")

    st.markdown("---")

    recommendation = recommendations.get(
        "recommended_target_architecture",
        "Unknown"
    )

    # Executive Summary
    st.subheader("📊 Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Architecture",
            architecture.get(
                "architecture_type",
                "Unknown"
            )
        )

    with col2:
        st.metric(
            "Domains",
            len(
                domains.get(
                    "domains",
                    []
                )
            )
        )

    with col3:
        st.metric(
            "Coupling Score",
            dependency.get(
                "coupling_score",
                0
            )
        )

    with col4:
        st.metric(
            "Target",
            recommendation
        )

    st.markdown("---")

    # Layer Statistics
    st.subheader("🏗️ Layer Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Controllers",
            repo.get(
                "controller_count",
                0
            )
        )

    with col2:
        st.metric(
            "Services",
            repo.get(
                "service_count",
                0
            )
        )

    with col3:
        st.metric(
            "Repositories",
            repo.get(
                "repository_count",
                0
            )
        )

    with col4:
        st.metric(
            "Entities",
            repo.get(
                "entity_count",
                0
            )
        )

    st.markdown("---")

    # Dependency Statistics
    st.subheader("🔗 Dependency Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Nodes",
            dependency.get(
                "node_count",
                0
            )
        )

    with col2:
        st.metric(
            "Edges",
            dependency.get(
                "edge_count",
                0
            )
        )

    with col3:
        st.metric(
            "Coupling",
            dependency.get(
                "coupling_score",
                0
            )
        )

    st.markdown("---")

    # Architecture Recommendation
    st.subheader("🤖 AI Recommendation")

    st.success(
        f"Recommended Architecture: "
        f"{recommendation}"
    )

    if "migration_complexity" in recommendations:

        st.info(
            f"Migration Complexity: "
            f"{recommendations['migration_complexity']}"
        )

    if "confidence" in recommendations:

        st.info(
            f"Confidence Score: "
            f"{recommendations['confidence']}%"
        )

    st.markdown("---")

    # Domains
    st.subheader("📦 Detected Business Domains")

    for domain in domains.get(
        "domains",
        []
    ):

        st.write(
            f"✅ {domain['name']}"
        )

    st.markdown("---")

    # Reasoning
    st.subheader("🧠 Recommendation Reasoning")

    for reason in recommendations.get(
        "reasoning",
        []
    ):

        st.write(
            f"• {reason}"
        )