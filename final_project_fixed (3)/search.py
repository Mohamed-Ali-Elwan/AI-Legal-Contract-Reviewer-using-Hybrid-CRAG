from langchain_tavily import TavilySearch


class Search:

    def __init__(self, api_key: str):
        self.api_key = api_key

        # Trusted Egyptian legal sources
        self.allowed_domains = [
           # Official government (.gov.eg)
            "moj.gov.eg",           # Ministry of Justice
            "parliament.gov.eg",    # House of Representatives - official legislation
            "sce.gov.eg",           # State Council - administrative law & rulings
            "cc.gov.eg",            # Supreme Constitutional Court
            "moi.gov.eg",           # Ministry of Interior - criminal procedure
            "ppo.gov.eg",           # Personal Data Protection Center
            "gafi.gov.eg",          # General Authority for Investment - contract/company law
            "fra.gov.eg",           # Financial Regulatory Authority
            "sis.gov.eg",           # State Information Service

            # Official but not .gov.eg
            "cbe.org.eg",           # Central Bank of Egypt - banking law

            # Authoritative legal databases (non-government but widely cited)
            "eastlaws.com",         # Largest Arabic legal database (statutes, rulings)
            "manshurat.org",        # MENA legislation database (Bibliotheca Alexandrina)
            "wipolex.wipo.int",     # Official IP/copyright law texts
            "ilo.org",              # NATLEX - official labor law texts
        ]

        # `langchain_tavily.TavilySearch` is a LangChain Runnable/Tool - it has
        # no `.search()` method (that belongs to the raw `tavily-python`
        # TavilyClient). It's called with `.invoke(...)`, and its constructor
        # kwarg is `tavily_api_key`, not `api_key`. `max_results` is only
        # accepted at construction time - passing it again on invoke() raises
        # a ValueError ("can only be set during instantiation").
        self.client = TavilySearch(
            tavily_api_key=api_key,
            max_results=5,
            search_depth="advanced",
            include_domains=self.allowed_domains
        )

    def search(self, query: str):

        response = self.client.invoke({"query": query})

        results = response.get("results", []) if isinstance(response, dict) else []

        filtered_results = []

        for result in results:

            url = result.get("url", "").lower()

            if any(domain in url for domain in self.allowed_domains):
                filtered_results.append(result)

        return filtered_results
