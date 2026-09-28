``
# 🏥 Agentic Healthcare Assistant

An AI-powered healthcare assistant developed as an IIT GenAI Capstone Project. The application uses **Retrieval-Augmented Generation (RAG)**, **semantic search**, and **Large Language Models (LLMs)** to provide contextual responses to healthcare-related queries.

---

## 📌 Project Overview

The Agentic Healthcare Assistant demonstrates how Generative AI and Retrieval-Augmented Generation can be applied to a healthcare-oriented use case.

The system retrieves relevant information from a vector store using semantic similarity search and provides the retrieved context to an OpenAI language model to generate a natural-language response.

The application is built with a modular architecture consisting of:

- Healthcare agent logic
- RAG pipeline
- FAISS vector store
- Hugging Face embeddings
- OpenAI LLM integration
- Streamlit user interface

---

## 🎯 Objectives

The main objectives of this project are:

- Implement a Retrieval-Augmented Generation (RAG) pipeline.
- Use vector embeddings for semantic search.
- Store and retrieve healthcare-related information using FAISS.
- Integrate an OpenAI language model for response generation.
- Build an interactive healthcare assistant using Streamlit.
- Demonstrate an extensible architecture for future agentic AI capabilities.

---

## ✨ Key Features

### 🔎 Semantic Search

Healthcare information is converted into vector embeddings using the Hugging Face:

```text
sentence-transformers/all-MiniLM-L6-v2
````

 The embeddings are stored in a FAISS vector store for similarity-based retrieval.

 ### 🤖 Retrieval-Augmented Generation

 The system retrieves relevant information from the vector store and provides it as context to the language model before generating a response.

 ### 🧠 Vector Memory

 FAISS is used to store and retrieve semantically similar documents.

 ### 💬 Natural Language Responses

 OpenAI is used to generate responses based on the retrieved information.

 ### 🖥️ Streamlit Interface

 The application provides a simple web-based interface for interacting with the healthcare assistant.

---

 ## 🏗️ System Architecture

```
                 ┌───────────────────┐
                 │       User        │
                 │      Query        │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    Streamlit      │
                 │   User Interface  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   Disease Agent   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    RAG Search     │
                 │     Pipeline      │
                 └─────────┬─────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
     ┌─────────────────┐      ┌─────────────────┐
     │  FAISS Vector   │      │   OpenAI LLM    │
     │      Store      │      │   Generation     │
     └────────┬────────┘      └────────┬────────┘
              │                        │
              ▼                        │
     ┌─────────────────┐               │
     │ Hugging Face    │               │
     │   Embeddings    │               │
     └─────────────────┘               │
              │                        │
              └───────────┬────────────┘
                          ▼
                 ┌───────────────────┐
                 │ Context-Aware     │
                 │     Response      │
                 └───────────────────┘
```

---

 ## 🛠️ Technology Stack

 | Technology | Purpose |
| --- | --- |
| Python | Application development |
| Streamlit | Web interface |
| LangChain | RAG and LLM orchestration |
| LangChain Classic | RetrievalQA integration |
| LangChain Community | FAISS and embedding integrations |
| OpenAI | Language model |
| FAISS | Vector similarity search |
| Hugging Face | Text embeddings |
| Sentence Transformers | Embedding model |
| python-dotenv | Environment configuration |

---

 ## 📁 Project Structure

```
agentic-healthcare-assistant/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── src/
    │
    ├── agents/
    │   └── disease_agent.py
    │
    ├── memory/
    │   └── vector_store.py
    │
    ├── rag_pipeline/
    │   └── rag_search.py
    │
    └── userinterface/
        └── app.py
```

 ### Main Components

 **`disease_agent.py`**

 Contains the healthcare agent logic used by the application.

 **`vector_store.py`**

 Responsible for:

 - Creating Hugging Face embeddings
- Building the FAISS vector store
- Performing semantic similarity searches

 **`rag_search.py`**

 Implements the Retrieval-Augmented Generation workflow by:

 - Loading the OpenAI API key
- Initializing the vector store
- Retrieving relevant information
- Passing retrieved context to the OpenAI model
- Generating the final response

 **`app.py`**

 Provides the Streamlit-based user interface.

---

 ## ⚙️ Installation

 ### 1\. Clone the Repository

```
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd agentic-healthcare-assistant
```

 ### 2\. Create a Virtual Environment

 For Windows:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

 For Linux/macOS:

```
python3 -m venv .venv
source .venv/bin/activate
```

 ### 3\. Install Dependencies

```
pip install -r requirements.txt
```
streamlit run src/userinterface/app.py
```

 Streamlit will provide a local URL where the application can be accessed in a web browser.

---

 ## 💡 Example Workflow

 A typical interaction follows this process:

```
User Query
    ↓
Streamlit Interface
    ↓
Disease Agent
    ↓
RAG Pipeline
    ↓
Semantic Search
    ↓
FAISS Vector Store
    ↓
Relevant Documents
    ↓
OpenAI LLM
    ↓
Generated Response
```

 Example query:

```
What are the treatment options for chronic kidney disease?
```

 The system retrieves relevant information from the vector store and uses that information as context for generating a response.

---

 ## 🎓 Academic Project

 **Project:** Agentic Healthcare Assistant\
 **Program:** IIT GenAI Course\
 **Project Type:** Capstone Project

---

 ## 👨‍💻 Author

 **\[Suruthi Lakshmi M\]**

 IIT GenAI Course – Capstone Project

```
agentic-healthcare-assistant
│
├── README.md             ← this file
├── requirements.txt
├── src/
│   ├── agents/
│   ├── memory/
│   ├── rag_pipeline/
│   └── userinterface/
│
└── .env  
```