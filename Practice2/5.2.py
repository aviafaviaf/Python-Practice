a = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407, 6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903, 2067967, 2068456]


def decode_val(y):
    y = bin(y)[2:]
    result = ""
    for i in range(0, len(y), 3):
        result += "1" if sum(map(int, y[i:i + 3])) >= 2 else "0"
    return chr(int(result, 2))


message = ""
for x in a:
    message += decode_val(x)
print(message)