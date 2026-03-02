import logging
from ingestion import load_and_chunk_cv
from retriever import create_vector_store, get_retriever
from tools import cv_search_tool
from memory import get_memory
from agent import create_agent
from output_writer import write_output
from logger import setup_logger

def main():
    setup_logger()

    chunks = load_and_chunk_cv()
    vectorstore = create_vector_store(chunks)
    retriever = get_retriever(vectorstore)

    tool = cv_search_tool(retriever)
    memory = get_memory()
    agent = create_agent(tool, memory)

    print("CV Agent Ready. Type 'exit' to quit.\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break

        response = agent.run(query)
        print(f"\nAgent: {response}\n")

        write_output(query, response)

if __name__ == "__main__":
    main()
