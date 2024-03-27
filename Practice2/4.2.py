from ctypes import c_uint32


def decrypt(v, k):
    v0 = c_uint32(v[0])
    v1 = c_uint32(v[1])
    s = 0xC6EF3720
    delta = 0x9E3779B9
    k0 = k[0]
    k1 = k[1]
    k2 = k[2]
    k3 = k[3]

    for i in range(32):
        v1.value -= ((v0.value << 4) + k2) ^ (v0.value + s) ^ ((v0.value >> 5) + k3)
        v0.value -= ((v1.value << 4) + k0) ^ (v1.value + s) ^ ((v1.value >> 5) + k1)
        s -= delta

    return v0.value, v1.value


KEY = [0, 4, 5, 1]
message = '''
E3238557 6204A1F8 E6537611 174E5747
5D954DA8 8C2DFE97 2911CB4C 2CB7C66B
E7F185A0 C7E3FA40 42419867 374044DF
2519F07D 5A0C24D4 F4A960C5 31159418
F2768EC7 AEAF14CF 071B2C95 C9F22699
FFB06F41 2AC90051 A53F035D 830601A7
EB475702 183BAA6F 12626744 9B75A72F
8DBFBFEC 73C1A46E FFB06F41 2AC90051
97C5E4E9 B1C26A21 DD4A3463 6B71162F
8C075668 7975D565 6D95A700 7272E637
'''
message_list = list(map(lambda s: int(s, 16), message.split()))

res = []
for i in range(0, len(message_list), 2):
    res += decrypt(message_list[i:i + 2], KEY)

''.join(map(chr, res))