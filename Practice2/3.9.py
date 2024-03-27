def rle_encode(s):
    return [(s[i], i - [j for j in range(i, -1, -1) if s[j] != s[i] or j == 0][0] + (1 if i == 0 else 0)) for i in range(len(s)) if i + 1 < len(s) and s[i + 1] != s[i] or i + 1 == len(s)]

print(rle_encode('ABBCCCDEF'))
