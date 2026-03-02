from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import settings
import logging

logger = logging.getLogger(__name__)

def load_and_chunk_cv():
    try:
        logger.info("Loading CV...")
        loader = PyPDFLoader(settings.CV_PATH)
        documents = loader.load()

        logger.info("Splitting CV into chunks...")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

        chunks = splitter.split_documents(documents)
        logger.info(f"Total chunks created: {len(chunks)}")

        return chunks

    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        raise
