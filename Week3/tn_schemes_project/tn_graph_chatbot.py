import os
import networkx as nx
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TN Schemes GraphRAG Explorer",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main { background-color: #f4f6f9; }
    .hero-box {
        padding: 2rem;
        background: linear-gradient(135deg, #2c3e50 0%, #4ca1af 100%);
        color: white;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR CONTROL PANEL ---
with st.sidebar:
  st.title("Graph Control Panel")
  if os.getenv("OPENAI_API_KEY"):
    st.success("🔑 API Key active!")
  else:
    st.error("⚠️ OPENAI_API_KEY missing in .env")

  st.divider()
  st.markdown("### 🕸️ Graph Intelligence")
  st.info(
      "Unlike Vector RAG, this engine structures scheme data into interconnected"
      " web nodes and relationships."
  )

# --- HERO HEADER ---
st.markdown(
    """
    <div class="hero-box">
        <h1>🕸️ Tamil Nadu Schemes GraphRAG Explorer</h1>
        <p style='font-size: 1.1rem; opacity: 0.9;'>Powered by NetworkX & LLM Graph Extraction. Queries navigate entity relationships instead of raw text proximity.</p>
    </div>
""",
    unsafe_allow_html=True,
)


# --- KNOWLEDGE GRAPH CONSTRUCTION (CACHED) ---
@st.cache_resource
def build_knowledge_graph():
  target_url = "https://www.tn.gov.in/schemes.php"
  loader = WebBaseLoader(target_url)
  docs = loader.load()

  # Split text into chunks to respect token windows for extraction
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=1500, chunk_overlap=200
  )
  chunked_docs = text_splitter.split_documents(docs)

  # Initialize LLM and Graph Transformer
  api_key = os.getenv("OPENAI_API_KEY")
  llm = ChatOpenAI(
      model="gpt-4o-mini", temperature=0, openai_api_key=api_key
  )
  transformer = LLMGraphTransformer(llm=llm)

  # Extract graph documents (Nodes & Relationships)
  # Limiting to first 3 chunks to optimize build time for initial testing
  graph_documents = transformer.convert_to_graph_documents(chunked_docs[:3])

  # Build NetworkX Directed Graph
  knowledge_graph = nx.DiGraph()

  for g_doc in graph_documents:
    for node in g_doc.nodes:
      knowledge_graph.add_node(node.id, type=node.type)
    for rel in g_doc.relationships:
      knowledge_graph.add_edge(
          rel.source.id, rel.target.id, relationship=rel.type
      )

  return knowledge_graph, graph_documents


with st.spinner(
    "🔄 Extracting entities and mapping relationships into a Knowledge Graph..."
):
  try:
    nx_graph, raw_graph_docs = build_knowledge_graph()
    st.success(
        f"✅ Knowledge Graph successfully built! Nodes: {nx_graph.number_of_nodes()}"
        f" | Edges: {nx_graph.number_of_edges()}"
    )
  except Exception as e:
    st.error(f"Error building knowledge graph: {e}")
    st.stop()

# --- SIDEBAR GRAPH METRICS ---
with st.sidebar:
  st.metric("Total Entities (Nodes)", nx_graph.number_of_nodes())
  st.metric("Total Relationships (Edges)", nx_graph.number_of_edges())
  with st.expander("View Extracted Entities"):
    st.write(list(nx_graph.nodes)[:20])


# --- GRAPH-AWARE CONTEXT RETRIEVAL ---
def get_graph_context(query):
  # Search nodes matching query keywords to fetch immediate neighbors
  query_tokens = query.lower().split()
  relevant_context = []

  for node in nx_graph.nodes:
    if any(token in node.lower() for token in query_tokens):
      # Get neighbors and relationship types
      neighbors = nx_graph.neighbors(node)
      for n in neighbors:
        edge_data = nx_graph.get_edge_data(node, n)
        rel = edge_data.get("relationship", "RELATED_TO")
        relevant_context.append(f"({node}) --[{rel}]--> ({n})")

      # Also check incoming edges
      predecessors = nx_graph.predecessors(node)
      for p in predecessors:
        edge_data = nx_graph.get_edge_data(p, node)
        rel = edge_data.get("relationship", "RELATED_TO")
        relevant_context.append(f"({p}) --[{rel}]--> ({node})")

  if not relevant_context:
    # Fallback to general graph summary if no direct node hit
    return (
        "General Graph Structure Summary: "
        + str(list(nx_graph.edges(data=True))[:15])
    )

  return "\n".join(list(set(relevant_context))[:15])


# --- RAG GENERATION SETUP ---
def generate_graph_response(user_query):
  api_key = os.getenv("OPENAI_API_KEY")
  llm = ChatOpenAI(
      model="gpt-4o-mini", temperature=0.2, openai_api_key=api_key
  )

  graph_context = get_graph_context(user_query)

  system_prompt = (
      "You are an expert graph intelligence assistant for Tamil Nadu Government"
      " schemes.\nAnswer the user query strictly using the provided Knowledge"
      " Graph relational paths.\n\nGraph Context Triples:\n{context}"
  )

  prompt = ChatPromptTemplate.from_messages([
      ("system", system_prompt),
      ("human", "{input}"),
  ])

  chain = prompt | llm
  response = chain.invoke({"context": graph_context, "input": user_query})
  return response.content


# --- STREAMLIT CHAT INTERFACE ---
if "graph_messages" not in st.session_state:
  st.session_state.graph_messages = [{
      "role": "assistant",
      "content": (
          "Hello! I am your TN Schemes Knowledge Graph Assistant. Ask me about"
          " specific schemes or entity connections!"
      ),
  }]

for message in st.session_state.graph_messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

user_query = st.chat_input("Ask a question about scheme relationships...")

if user_query:
  st.session_state.graph_messages.append(
      {"role": "user", "content": user_query}
  )
  with st.chat_message("user"):
    st.markdown(user_query)

  with st.chat_message("assistant"):
    with st.status(
        "🔍 Traversing knowledge graph nodes & relationships...", expanded=False
    ) as status:
      answer = generate_graph_response(user_query)
      status.update(label="✨ Graph-driven answer generated!", state="complete")

    st.markdown(answer)
    st.session_state.graph_messages.append(
        {"role": "assistant", "content": answer}
    )