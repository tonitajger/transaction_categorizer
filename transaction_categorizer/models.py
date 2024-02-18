from enum import Enum

from config import load_secrets
from langchain_community.chat_models import ChatOllama
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI

SECRETS = load_secrets()
OPENAI_API_KEY = SECRETS.get("OPENAI_API_KEY")

TEMPERATURE = 0


class ModelChoice(Enum):
    llama2 = "llama2"
    gpt4 = "gpt4"


def supports_function_calling(model: BaseChatModel):
    return hasattr(model, "bind_functions")


def model_factory(model: ModelChoice):
    if model == ModelChoice.llama2:
        return ChatOllama(model="llama2", temperature=TEMPERATURE)
    elif model == ModelChoice.gpt4:
        return ChatOpenAI(
            model="gpt-4", temperature=TEMPERATURE, openai_api_key=OPENAI_API_KEY
        )
    else:
        raise ValueError(f"Model {model} not supported")
