class Planner:
    def decompose(self, query: str):
        query_lower = query.lower()
        if "book" in query_lower or "appointment" in query_lower:
            return [{"task": "book_appointment"}]
        elif "history" in query_lower or "record" in query_lower:
            return [{"task": "retrieve_history"}]
        elif "summarize" in query_lower or "latest" in query_lower or "treatment" in query_lower:
            return [{"task": "search_disease_info"}]
        else:
            return [{"task": "unknown"}]