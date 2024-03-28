def ham_dist(x, y):
    return sum(1 for i in range(len(bin(x)[2:].rjust(32, "0"))) if bin(x)[2:].rjust(32, "0")[i] != bin(y)[2:].rjust(32, "0")[i])


print(ham_dist(0b10, 0b11))
print(ham_dist(0b1100, 0b0011))
