from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from config import settings
import logging

logger = logging.getLogger(__name__)

def create_vector_store(chunks):
    logger.info("Creating embeddings and vector store...")
    embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_kwargs={"k": settings.RETRIEVAL_TOP_K}
    )
