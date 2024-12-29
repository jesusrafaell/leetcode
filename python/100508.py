class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        cache = {}

        def dfs(i, s, curr):
            # nonlocal ans
            if (i, s, curr) in cache:
                return cache[(i, s, curr)]

            if s == numFriends - 1:
                ans = max(curr, max(curr, word[i:]))
                cache[(i, s, curr)] = ans
                return ans

            res = ""
            for e in range(i + 1, len(word) - (numFriends - s - 1) + 1):
                t = dfs(e, s + 1, max(curr, word[i:e]))
                res = max(res, t)

            cache[(i, s, curr)] = res
            return res

        return dfs(0, 0, "")


"""
input:
1)
"dbca" 
2

2)
"gggg" 
4
"""
