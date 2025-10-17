def solve(s: str) -> str:
    if len(s) == 0: return ""
    
    # Вычисляем префикс-функцию
    pi = [0] * len(s)
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]: j += 1
        pi[i] = j

    # В последнем элементе префикс-функции будет длина
    # наибольшего суффикса, который также является префиксом
    return s[:pi[-1]]

test_cases = ["abacaba", "aaabbaaa", "azaza", "a", "ab", "aa", ""]
    
for s in test_cases:
    print(f"### test {s} ###")
    print(solve(s))
