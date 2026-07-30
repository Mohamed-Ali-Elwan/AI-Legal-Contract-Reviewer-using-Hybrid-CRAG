from langchain_core.prompts import PromptTemplate


class PromptBuilder:

    @staticmethod
    def review_prompt() -> PromptTemplate:

        template = """
                You are an expert legal assistant specializing in Egyptian contract law.

                IMPORTANT LANGUAGE INSTRUCTIONS:

                - Answer ONLY in Egyptian Arabic.
                - Write naturally in Egyptian Arabic.
                - Do NOT use English except for legal article numbers if necessary.
                - Keep all explanations, recommendations, summaries, and risk descriptions in Egyptian Arabic.
                - The JSON keys must remain in English exactly as specified.
                - Only the VALUES should be in Egyptian Arabic.

                Return ONLY valid JSON.

                Your task is to analyse the uploaded contract.

                Use ONLY the provided legal references.

                ========================
                Contract
                ========================

                {contract}

                ========================
                Legal References
                ========================

                {context}

                ========================
                Instructions
                ========================

                1. Summarise the contract.
                2. Identify risky clauses.
                3. Explain every risk.
                4. Suggest improvements.
                5. Give an overall risk level.

                {format_instructions}
                """

        return PromptTemplate(
            template=template,
            input_variables=[
                "contract",
                "context",
                "format_instructions"
            ]
        )
        # NOTE: format_instructions used to be declared as a `partial_variables`
        # entry whose value was the literal string "{format_instructions}" -
        # that baked the placeholder text itself into the template instead of
        # the real schema text, and since it wasn't in input_variables the
        # value service.py passed in at call time was silently dropped.

    ##################################################################

    @staticmethod
    def clause_extraction_prompt() -> PromptTemplate:

        template = """
            You are an expert legal assistant specialising in Egyptian contract law.
            IMPORTANT LANGUAGE INSTRUCTIONS:
            
             - Answer ONLY in Egyptian Arabic.
             - Write naturally in Egyptian Arabic.
             - Do NOT use English except for legal article numbers if necessary.
             - Keep all explanations, recommendations, summaries, and risk descriptions in Egyptian Arabic.
             - The JSON keys must remain in English exactly as specified.
             - Only the VALUES should be in Egyptian Arabic.
            

            Read the contract below and extract the key clauses that need a
            legal risk review (e.g. termination, liability, payment,
            confidentiality, penalties, dispute resolution, indemnity).

            ========================
            Contract
            ========================

            {contract}

            Return the clauses as a plain numbered list, one clause per line.
            Do not add commentary or explanations - clauses only.
            """

        return PromptTemplate(
            template=template,
            input_variables=["contract"]
        )

    ##################################################################

    @staticmethod
    def search_prompt() -> PromptTemplate:

        template = """
            Generate ONE search query for Egyptian law.
            IMPORTANT LANGUAGE INSTRUCTIONS:
                        
                         - Answer ONLY in Egyptian Arabic.
                         - Write naturally in Egyptian Arabic.
                         - Do NOT use English except for legal article numbers if necessary.
                         - Keep all explanations, recommendations, summaries, and risk descriptions in Egyptian Arabic.
                         - The JSON keys must remain in English exactly as specified.
                         - Only the VALUES should be in Egyptian Arabic.

            Clause

            {clause}

            Return ONLY the search query.
            """

        return PromptTemplate(
            template=template,
            input_variables=["clause"]
        )

    ##################################################################

    @staticmethod
    def summary_prompt() -> PromptTemplate:

        template = """
            Summarise the following contract.
            IMPORTANT LANGUAGE INSTRUCTIONS:
                        
                         - Answer ONLY in Egyptian Arabic.
                         - Write naturally in Egyptian Arabic.
                         - Do NOT use English except for legal article numbers if necessary.
                         - Keep all explanations, recommendations, summaries, and risk descriptions in Egyptian Arabic.
                         - The JSON keys must remain in English exactly as specified.
                         - Only the VALUES should be in Egyptian Arabic.

            Contract

            {contract}
            """

        return PromptTemplate(
            template=template,
            input_variables=["contract"]
        )

    ##################################################################

    @staticmethod
    def recommendation_prompt() -> PromptTemplate:

        template = """
            You are an expert legal assistant specialising in Egyptian contract law.
            IMPORTANT LANGUAGE INSTRUCTIONS:
                        
                         - Answer ONLY in Egyptian Arabic.
                         - Write naturally in Egyptian Arabic.
                         - Do NOT use English except for legal article numbers if necessary.
                         - Keep all explanations, recommendations, summaries, and risk descriptions in Egyptian Arabic.
                         - The JSON keys must remain in English exactly as specified.
                         - Only the VALUES should be in Egyptian Arabic.

            Given the risk described below and the relevant legal context,
            write one short, actionable recommendation to reduce or
            eliminate this risk.

            ========================
            Risk
            ========================

            {risk}

            ========================
            Legal Context
            ========================

            {context}

            Return ONLY the recommendation text.
            """

        return PromptTemplate(
            template=template,
            input_variables=["risk", "context"]
        )
