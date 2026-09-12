🏛️ TAMIL NADU SCHEMES GRAPHRAG EXPLORER

An advanced Knowledge Graph Retrieval-Augmented Generation (GraphRAG) assistant that extracts structured entities and semantic relationships from official Tamil Nadu government portal listings, allowing users to query data via relational graph traversal rather than standard text proximity matching.

KEY FEATURES:
- LLM-Powered Graph Extraction: Automatically parses raw government web pages using LangChain Experimental's LLMGraphTransformer to map out distinct entities (nodes) and their relationships (edges).
- NetworkX Relational Database: Builds and queries an in-memory directed graph (nx.DiGraph) to retrieve multi-hop context.
- Interactive Streamlit Interface: Features real-time node/edge telemetry metrics, collapsible metadata inspection panels, and modern chat containers.
- Secure Configuration: Uses python-dotenv for local environment variable management.

TECH STACK:
- Frontend/UX: Streamlit
- Graph Intelligence: NetworkX, LangChain Experimental (LLMGraphTransformer)
- Orchestration: LangChain, OpenAI API (gpt-4o-mini)
- Data Ingestion: BeautifulSoup4, LangChain Community (WebBaseLoader)
- Environment Management: Python-Dotenv

SETUP AND EXECUTION:
1. Create and activate a virtual environment (e.g., tn_schemes_env)
2. Install requirements: pip install streamlit networkx langchain langchain-experimental langchain-community langchain-openai beautifulsoup4 python-dotenv
3. Create a .env file containing your OPENAI_API_KEY
4. Run the app: streamlit run tn_graph_chatbot.py
