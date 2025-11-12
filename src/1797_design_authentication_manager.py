import heapq

# # hashmap
# class AuthenticationManager:
#     def __init__(self, timeToLive: int):
#         self.timeToLive = timeToLive
#         self.tokens = {}

#     def generate(self, tokenId: str, currentTime: int) -> None:
#         self.tokens[tokenId] = currentTime + self.timeToLive

#     def renew(self, tokenId: str, currentTime: int) -> None:
#         if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
#             self.tokens[tokenId] = currentTime + self.timeToLive

#     def countUnexpiredTokens(self, currentTime: int) -> int:
#         self._expireTokens(currentTime)
#         return len(self.tokens)

#     def _expireTokens(self, currentTime: int) -> None:
#         expiredTokens = []

#         for tokenId, expireTime in self.tokens.items():
#             if expireTime <= currentTime:
#                 expiredTokens.append(tokenId)

#         for tokenId in expiredTokens:
#             del self.tokens[tokenId]


# hashmap + heap
class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenIdToExpireTime = {}
        self.expiryQueue = []

    def generate(self, tokenId: str, currentTime: int) -> None:
        expireTime = currentTime + self.timeToLive
        self.tokenIdToExpireTime[tokenId] = expireTime
        heapq.heappush(self.expiryQueue, (expireTime, tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        if (
            tokenId in self.tokenIdToExpireTime
            and self.tokenIdToExpireTime[tokenId] > currentTime
        ):
            expireTime = currentTime + self.timeToLive
            self.tokenIdToExpireTime[tokenId] = expireTime
            heapq.heappush(self.expiryQueue, (expireTime, tokenId))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._expireTokens(currentTime)
        return len(self.tokenIdToExpireTime)

    def _expireTokens(self, currentTime: int) -> None:
        while self.expiryQueue and self.expiryQueue[0][0] <= currentTime:
            expireTime, tokenId = heapq.heappop(self.expiryQueue)

            # heap may contain stale entries for renewed tokens
            # don't use these stale entries to delete from the map
            if (
                tokenId in self.tokenIdToExpireTime
                and self.tokenIdToExpireTime[tokenId] == expireTime
            ):
                del self.tokenIdToExpireTime[tokenId]


def test_AuthenticationManager():
    obj = AuthenticationManager(5)
    obj.renew("aaa", 1)
    obj.generate("aaa", 2)
    assert obj.countUnexpiredTokens(6) == 1

    obj.generate("bbb", 7)
    obj.renew("aaa", 8)
    obj.renew("bbb", 10)
    assert obj.countUnexpiredTokens(15) == 0
