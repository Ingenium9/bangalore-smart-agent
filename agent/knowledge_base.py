from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os

def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load_and_split()

def build_vectorstore(pages):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(pages, embeddings)

def get_vectorstore():
    pdf_path = os.path.join("pdf", "The Ultimate Bangalore Guide.pdf")
    pages = load_pdf(pdf_path)
    return build_vectorstore(pages)
