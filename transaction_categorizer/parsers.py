from enum import Enum

from langchain.output_parsers import ResponseSchema, StructuredOutputParser


class ParserChoice(Enum):
    structured = "structured"


def parser_factory(choice: ParserChoice):
    if choice == ParserChoice.structured:
        response_schemas = [
            ResponseSchema(
                name="description",
                description="Original description of the transaction. Just pass input here description here",
            ),
            ResponseSchema(
                name="category", description="Parent category of the transaction"
            ),
            ResponseSchema(
                name="subcategory", description="Subcategory of the transaction"
            ),
            ResponseSchema(
                name="reasoning",
                description="Explanation of the transaction and why it's categorized as such",
            ),
        ]

        structured_parser = StructuredOutputParser.from_response_schemas(
            response_schemas
        )
        return structured_parser

    else:
        raise ValueError(f"Parser {choice} not supported")
