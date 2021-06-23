def longestPalindromeBruteForce(s: str) -> str:  # n^3
    best_len = 0
    best_s = ""
    n = len(s)
    for l in range(n):
        for r in range(l, n):
            substring = s[l:r + 1]
            if substring == substring[::-1]:
                if (len(substring) > best_len):
                    best_len = r - l + 1
                    best_s = substring
    return best_s


def longestPalindromBinsearch(s):
    best_len = 0
    best_s = ""
    n = len(s)
    for l in range(n):

        for r in range(l, n):
            substring = s[l:r + 1]
            if substring == substring[::-1]:
                if (len(substring) > best_len):
                    best_len = r - l + 1
                    best_s = substring
    return best_s


def longestPalindromWindow(s):
    res = ""
    for i in range(len(s)):
        res = max(palindrome(s, i, i), palindrome(s, i, i + 1), res, key=len)
    return res


def palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


print(longestPalindromeBruteForce("babad"))
