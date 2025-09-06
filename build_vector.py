import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

file_path = "resume.md"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"⚠️ Le fichier {file_path} est introuvable. Vérifie son emplacement.")

loader = TextLoader(file_path, encoding="utf-8")
docs = loader.load()

# Découpage en chunks plus grands pour améliorer la cohérence
splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=10)
chunks = splitter.split_documents(docs)

# ✅ Embeddings multilingues pour un meilleur support du français
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Création et sauvegarde de l’index vectoriel
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="chroma_index")
vectorstore.persist()

print("✅ Index Chroma (multilingue) créé et sauvegardé dans 'chroma_index'.")
