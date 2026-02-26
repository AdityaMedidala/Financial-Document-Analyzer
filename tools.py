## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

# FIX: Notice we are importing from 'crewai.tools', not 'crewai_tools'
from crewai.tools import tool

#added
from langchain_community.document_loaders import PyPDFLoader

# Fixed SerperDevTool import path for newer crewai_tools versions
from crewai_tools import SerperDevTool

#added
load_dotenv()


## Creating search tool
search_tool = SerperDevTool()



# FIX: Completely removed the "class FinancialDocumentTool:" wrapper.
# Added the @tool decorator so CrewAI recognizes it.
@tool("Read Financial Document")
def read_data_tool(file_path: str) -> str:
    """
    Tool to read text data from a PDF file.
    Pass the exact file_path of the PDF to read its contents.
    """
    try:
        # FIX: Replaced undefined 'Pdf' with PyPDFLoader
        loader = PyPDFLoader(file_path=file_path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content

            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report
    except Exception as e:
        return f"Error reading PDF file: {str(e)}"

## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    # Kept for your future use, but not currently used by CrewAI agents
    async def analyze_investment_tool(financial_document_data):
        processed_data = financial_document_data
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    # Kept for your future use, but not currently used by CrewAI agents
    async def create_risk_assessment_tool(financial_document_data):
        return "Risk assessment functionality to be implemented"



'''
@tool("Read Financial Document")
def read_data_tool(file_path: str) -> str:
    """
    Tool to read text data from a PDF file.
    Pass the exact file_path of the PDF to read its contents.
    """
    try:
        # FIX: Replaced undefined 'Pdf' with PyPDFLoader
        loader = PyPDFLoader(file_path=file_path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content

            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report
    except Exception as e:
        return f"Error reading PDF file: {str(e)}"


## Creating custom pdf reader tool
class FinancialDocumentTool():
    async def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file
        """
        
        docs = Pdf(file_path=path).load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report

## Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    async def create_risk_assessment_tool(financial_document_data):        
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"

'''