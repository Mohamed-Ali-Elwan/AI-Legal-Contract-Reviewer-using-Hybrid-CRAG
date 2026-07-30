from typing import List

from pydantic import BaseModel, Field

from langchain_core.output_parsers import  PydanticOutputParser


class Issue(BaseModel):

    clause: str = Field(description="Clause name")

    risk_level: str = Field(
        description="Low, Medium or High"
    )

    explanation: str

    recommendation: str


class ContractReview(BaseModel):

    summary: str

    overall_risk: str

    issues: List[Issue]


class OutputParser:

    def __init__(self):

        self.parser = PydanticOutputParser(
            pydantic_object=ContractReview
        )

    ############################################################

    def get_parser(self):

        return self.parser

    ############################################################

    def get_format_instructions(self):

        return self.parser.get_format_instructions()

    ############################################################

    def parse(self, response: str):

        return self.parser.parse(response)