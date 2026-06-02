import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


def render_dependency_graph(context):

    dependency = context.dependency_analysis
    repo = context.repository_analysis

    G = nx.DiGraph()

    node_types = {}

    for item in repo["controllers"]:
        node_types[item["name"]] = "controller"

    for item in repo["services"]:
        node_types[item["name"]] = "service"

    for item in repo["repositories"]:
        node_types[item["name"]] = "repository"

    for item in repo["entities"]:
        node_types[item["name"]] = "entity"

    for node in dependency["nodes"]:
        G.add_node(node)

    for edge in dependency["edges"]:
        G.add_edge(
            edge["source"],
            edge["target"]
        )

    color_map = []

    for node in G.nodes():

        node_type = node_types.get(node)

        if node_type == "controller":
            color_map.append("skyblue")

        elif node_type == "service":
            color_map.append("lightgreen")

        elif node_type == "repository":
            color_map.append("orange")

        elif node_type == "entity":
            color_map.append("salmon")

        else:
            color_map.append("gray")

    fig, ax = plt.subplots(
        figsize=(14, 10)
    )

    pos = nx.kamada_kawai_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=color_map,
        node_size=2500,
        font_size=8,
        arrows=True,
        ax=ax
    )

    st.subheader(
        "Dependency Graph"
    )

    st.pyplot(fig)

    st.markdown("""
### Legend

🔵 Controller

🟢 Service

🟠 Repository

🔴 Entity
""")