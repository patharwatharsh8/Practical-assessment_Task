from langchain.tools import Tool

def cv_search_tool(retriever):
    def search_cv(query: str):
        docs = retriever.get_relevant_documents(query)
        if not docs:
            return "NO_CONTEXT_FOUND"
        return "\n\n".join([doc.page_content for doc in docs])

    return Tool(
        name="CV_Search",
        func=search_cv,
        description="Searches the CV for relevant information."
    )
