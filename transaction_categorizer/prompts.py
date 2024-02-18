from langchain_core.prompts import PromptTemplate


def get_prompt(structured_parser):
    return PromptTemplate(
        template="""
        You are an personal financial assistant that categorizes 
        bank transfers for transactions in Sweden. The categories
        should be useful for managing and visualizing personal budget 
        and expenses. Categorize the following transaction: "{description}".
        {format_instructions}
        """,
        input_variables=["description"],
        partial_variables={
            "format_instructions": structured_parser.get_format_instructions()
        },
    )
