from config import format_categories_for_prompt, parse_categories
from langchain_core.prompts import PromptTemplate


def get_prompt(structured_parser):
    formatted_categories = format_categories_for_prompt(parse_categories())
    return PromptTemplate(
        template=f"""
        You are an personal financial assistant that categorizes 
        bank transfers for transactions in Sweden. The categories
        should be useful for managing and visualizing personal budget 
        and expenses. Categorize the following transaction: "{{description}}".
        {{format_instructions}}
        categories and subcategories should be one of the categories provided 
        in this definition: 
        {formatted_categories}
        """,
        input_variables=["description"],
        partial_variables={
            "format_instructions": structured_parser.get_format_instructions()
        },
    )
