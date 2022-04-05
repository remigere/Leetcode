class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for cpdomain in cpdomains:
            #cpdomain = cpdomain.split(".")
            indices = [i for i, x in enumerate(cpdomain) if x == " " or x == "."]
            count = int(cpdomain[:indices[0]])
            for index in indices:
                d[cpdomain[index + 1:]] += count
        return [str(count) + " " + domain for domain, count in d.items()]