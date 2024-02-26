import logging
import os

import typer
from models import ModelChoice, model_factory
from parsers import ParserChoice, parser_factory
from prompts import get_prompt
from rich import print
from rich.logging import RichHandler

logger = logging.getLogger(__name__)
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(
    level=LOG_LEVEL,
    handlers=[RichHandler()],
    format="%(message)s",
    datefmt="[%Y-%m-%dT%H:%M:%S%z]",
)


app = typer.Typer()


@app.command()
def categorize(
    description: str = typer.Option(
        ..., "-d", "--description", help="Description of the transaction"
    ),
    model_choice: str = typer.Option(
        "llama2",
        "-m",
        "--model",
        help="Model to use for categorization",
    ),
):
    model = model_factory(ModelChoice(model_choice))
    logger.info(f"Using {model=} for categorization")

    parser = parser_factory(ParserChoice.structured)

    prompt = get_prompt(parser)

    chain = prompt | model | parser
    response = chain.invoke({"description": description})
    print(response)


if __name__ == "__main__":
    app()
