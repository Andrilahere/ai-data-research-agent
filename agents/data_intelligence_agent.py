import logging
from agents.data_intelligence_agent import DataIntelligenceAgent
from agents.research_assistant_agent import ResearchAssistantAgent

# Configure logging (you can also configure this globally in app/main.py)
logging.basicConfig(level=logging.INFO, format="🔎 [%(levelname)s] %(message)s")

class OrchestratorAgent:
    def __init__(self):
        self.data_agent = DataIntelligenceAgent()
        self.research_agent = ResearchAssistantAgent()

    def route(self, file_path: str, query: str):
        """
        Routes the request to the right agent based on file type.
        :param file_path: Path to the uploaded file
        :param query: User's natural language question
        """
        logging.info(f"Routing request | file={file_path}, query='{query}'")

        if file_path.endswith((".csv", ".xls", ".xlsx")):
            logging.info("Using DataIntelligenceAgent")
            self.data_agent.load_data(file_path)
            return self.data_agent.query(query)

        elif file_path.endswith(".pdf"):
            logging.info("Using ResearchAssistantAgent")
            self.research_agent.load_pdf(file_path)

            if "summarize" in query.lower():
                logging.info("Action: Summarization")
                return {"summary": self.research_agent.summarize()}

            elif any(keyword in query.lower() for keyword in ["keyword", "method", "result"]):
                logging.info("Action: Keyword/Method Extraction")
                return {"extraction": self.research_agent.extract_keywords()}

            else:
                logging.info("Action: General Q&A")
                return {"answer": self.research_agent.query(query)}

        else:
            logging.error("Unsupported file type")
            return {"error": "Unsupported file type"}


