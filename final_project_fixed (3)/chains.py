from langchain_classic.chains import LLMChain

from prompts import PromptBuilder


class ReviewChains:
    """
    Takes any LangChain-compatible chat/LLM Runnable (e.g. the ChatAnthropic
    instance from llm.get_llm()) and builds all the prompt chains around it.

    No model-specific wrapper needed here anymore - that's what made the old
    local-Mistral setup fragile. Any LangChain Runnable llm works.
    """

    def __init__(self, llm):

        self.summary_chain = LLMChain(
            llm=llm,
            prompt=PromptBuilder.summary_prompt()
        )

        self.clause_chain = LLMChain(
            llm=llm,
            prompt=PromptBuilder.clause_extraction_prompt()
        )

        self.search_chain = LLMChain(
            llm=llm,
            prompt=PromptBuilder.search_prompt()
        )

        self.review_chain = LLMChain(
            llm=llm,
            prompt=PromptBuilder.review_prompt()
        )

        self.recommendation_chain = LLMChain(
            llm=llm,
            prompt=PromptBuilder.recommendation_prompt()
        )
