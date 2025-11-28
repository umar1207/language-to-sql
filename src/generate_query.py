from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_query(question, context):
    PROMPT = f"""
        You are an expert SQL query generator.
        
        Use ONLY the PostgreSQL schema provided in the context.
        
        Context:
        {context}
        
        Question:
        {question}
        
        If schema does not match the questions then just RETURN 0
        Else Return ONLY SQL. 
        No explanation. No backticks.
    """

    llm = ChatOpenAI(model="gpt-4o-mini")
    query = llm.invoke(PROMPT).content.strip()
    return query
