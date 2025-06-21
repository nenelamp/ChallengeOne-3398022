from bisect import bisect_left
from typing import List

class SearchSuggestionSystem:
    def __init__(self, products: List[str]):
        
        self.products = sorted(products)

    def getSuggestions(self, searchWord: str) -> List[List[str]]:
        from bisect import bisect_left
        
        suggestions = []
        prefix = ""

        for char in searchWord:
            prefix += char
            
            i = bisect_left(self.products, prefix)
            group = []

           
            for j in range(i, min(i + 3, len(self.products))):
                if self.products[j].startswith(prefix):
                    group.append(self.products[j])
                else:
                    break
            suggestions.append(group)

        return suggestions

products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

system = SearchSuggestionSystem(products)
result = system.getSuggestions(searchWord)

for i, line in enumerate(result, 1):
    print(f"Step {i}: {line}")
