
import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain


class ResearchAssistantAgent:
    def __init__(self):
        self.docs = None
        self.db = None

    def load_pdf(self, file_path: str):
        text = ""
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()

        self.docs = text
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        self.db = FAISS.from_texts(chunks, embeddings)

        return f"PDF loaded with {len(chunks)} chunks"

    def summarize(self):
        llm = ChatOpenAI(model="gpt-5")
        return llm.predict(f"Summarize this research paper in <200 words:\n\n{self.docs[:3000]}")

    def extract_keywords(self):
        llm = ChatOpenAI(model="gpt-5")
        return llm.predict(f"Extract keywords, methods, and results from this paper:\n\n{self.docs[:3000]}")

    def query(self, question: str):
        retriever = self.db.as_retriever(search_kwargs={"k": 3})
        llm = ChatOpenAI(model="gpt-5")
        chain = load_qa_chain(llm, chain_type="stuff")
        docs = retriever.get_relevant_documents(question)
        return chain.run(input_documents=docs, question=question)

