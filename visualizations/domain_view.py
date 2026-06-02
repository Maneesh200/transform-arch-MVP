import streamlit as st


def render_domain_view(context):

    st.subheader("📦 Domain Architecture View")

    domains = context.domain_analysis.get(
        "domains",
        []
    )

    if not domains:

        st.warning(
            "No domains detected."
        )

        return

    for domain in domains:

        domain_name = domain.get(
            "name",
            "Unknown"
        )

        classes = domain.get(
            "classes",
            []
        )

        controllers = []
        services = []
        repositories = []
        entities = []

        for cls in classes:

            if "Controller" in cls:
                controllers.append(cls)

            elif "Service" in cls:
                services.append(cls)

            elif "Repository" in cls:
                repositories.append(cls)

            else:
                entities.append(cls)

        with st.container():

            st.markdown("---")

            st.markdown(
                f"## 🏢 {domain_name} Domain"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.info("🎮 Controllers")

                for item in controllers:
                    st.write(item)

            with col2:

                st.success("⚙️ Services")

                for item in services:
                    st.write(item)

            with col3:

                st.warning("🗄️ Repositories")

                for item in repositories:
                    st.write(item)

            with col4:

                st.error("📄 Entities")

                for item in entities:
                    st.write(item)

            st.markdown(
                """
                ### Flow

                Controller
                ↓

                Service
                ↓

                Repository
                ↓

                Entity
                """
            )