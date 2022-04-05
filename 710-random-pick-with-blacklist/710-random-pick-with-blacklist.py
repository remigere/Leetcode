class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        # The idea is if we have N=4 and blacklist = [0,2], then we need to
        # select from N-1-len(blacklist) things. We can do this by choosing
        # a random number on [0,N-1-len(blacklist)], but some of these may
        # not be allowed. Fix this by mapping them to allowed numbers from
        # the end of the range. So 0 -> 3, 1 is just itself, and higher things
        # don't matter because we're fully mapped.
        self.map = {}
        blacklist = set(blacklist) # to make membership an O(1) operation
        end = N-1 # a candidate "map to" number
        self.size = N - 1 - len(blacklist) # so we can know where to randomly sample from
        
        for x in blacklist:
            if x <= self.size:
                while end in blacklist: # find a number that's actually gucci to map to
                    end -= 1
                self.map[x] = end # map the unallowed number to the allowed number
                end -= 1 # consider next maybe-allowed number
        
        print(self.map)

    def pick(self) -> int:
        p = random.randint(0, self.size) # randomly sample
        if p in self.map: # oops, we chose a blacklisted one. Get the associated good one
            return self.map[p]
        else: # We chose a good one, so just return it.
            return p


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()