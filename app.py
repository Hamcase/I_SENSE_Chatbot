import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA, LLMChain
from langchain.prompts import PromptTemplate

# --- Custom CSS for Enhanced UI ---
st.markdown("""
    <style>
    /* General styling */
    body {
        font-family: 'Inter', sans-serif;
        background-color: #f5f7fa;
    }
    .stApp {
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    .stTitle {
        color: #1a3c6e;
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .stMarkdown {
        color: #333;
        font-size: 1.1em;
    }
    /* Chat messages */
    .stChatMessage {
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
    }
    .stChatMessage.user {
        background-color: #e6f3ff;
        border-left: 4px solid #1a73e8;
    }
    .stChatMessage.assistant {
        background-color: #f0f4f8;
        border-left: 4px solid #34c759;
    }
    /* Buttons */
    .stButton > button {
        background-color: #1a73e8;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 500;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1557b0;
    }
    /* Expander for sources */
    .stExpander {
        background-color: #fafafa;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    .stExpander summary {
        font-weight: 600;
        color: #1a3c6e;
    }
    /* Spinner */
    .stSpinner {
        color: #1a73e8;
    }
    /* Chat input */
    .stChatInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #d1d5db;
        padding: 12px;
        font-size: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# --- Configuration Streamlit ---
st.set_page_config(page_title="Chatbot I-SENSE", page_icon="🤖")
st.title("🤖 Chatbot I-SENSE")
st.markdown("Pose tes questions sur la plateforme I-SENSE.", unsafe_allow_html=True)

# --- Chargement de l'index vectoriel ---
@st.cache_resource
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    return Chroma(persist_directory="chroma_index", embedding_function=embeddings)

# --- Prompt strict FR + basé-docs uniquement ---
QA_PROMPT = PromptTemplate(
    template=(
        """
        Tu es un assistant basé uniquement sur des documents fournis.
        Si tu ne trouves pas la réponse dans les documents, réponds honnêtement : "Je ne sais pas."
        Répond uniquement à la question posée, n'ajoute pas d'autres informations qui ne concernent pas la question.
        Répond uniquement à la question posée, sans ajouter d'autres informations ou détails qui ne sont pas présents dans les documents suivants : 
        {context}

        Question : {question}

        Réponse :
        """),
    input_variables=["context", "question"],
)
#🔹 Donne uniquement l'idée principale de manière simple et claire.
# --- Prompt pour résumé (post-traitement) ---
SUMMARY_PROMPT = PromptTemplate(
    template=(
        """
        Résume le texte suivant en 2-3 phrases claires et concises en français : 
        {text}
        """),
    input_variables=["text"]
)

# --- Création de la chaîne QA (RetrievalQA) ---
@st.cache_resource
def create_chain():
    llm = OllamaLLM(model="mistral", temperature=0)  # temp=0 pour éviter l'impro
    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "fetch_k": 20, "lambda_mult": 0.5}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": QA_PROMPT},
        return_source_documents=True
    )
    return qa_chain

qa_chain = create_chain()
llm_for_summary = OllamaLLM(model="llama3", temperature=0)
summary_chain = LLMChain(llm=llm_for_summary, prompt=SUMMARY_PROMPT)

# --- État de session pour l'historique d'affichage (UI chat seulement) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Bouton reset ---
if st.button("🔄 Réinitialiser la discussion"):
    st.session_state.messages = []
    st.success("Discussion réinitialisée ✅", icon="✅")

# --- Affichage historique (UI) ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# --- Entrée utilisateur ---
if prompt := st.chat_input("💬 Ta question :"):
    st.chat_message("user").markdown(prompt, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Réflexion en cours..."):
        result = qa_chain.invoke({"query": prompt})
        answer = result.get("result", "").strip()

    # Affiche la réponse
    with st.chat_message("assistant"):
        st.markdown(answer if answer else "Je ne sais pas.", unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": answer if answer else "Je ne sais pas."})

    # Sources (passages utilisés)
    with st.expander("📚 Sources utilisées :"):
        srcs = result.get("source_documents", []) or []
        if not srcs:
            st.markdown("_Aucune source pertinente retrouvée._", unsafe_allow_html=True)
        else:
            for i, doc in enumerate(srcs, start=1):
                meta = doc.metadata if hasattr(doc, "metadata") else {}
                titre = meta.get("source") or meta.get("file_path") or meta.get("title") or "Document"
                page = meta.get("page", None)
                header = f"**Source {i} — {titre}" + (f" (page {page})**" if page is not None else "**")
                st.markdown(header, unsafe_allow_html=True)
                st.markdown(doc.page_content[:1500] + ("..." if len(doc.page_content) > 1500 else ""), unsafe_allow_html=True)