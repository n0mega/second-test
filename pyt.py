def reverse(x):
    return x[::-1]


def cheack_plaindorme(s):
    result = []
    for i in len(s):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if reverse(sub):
                result.append(sub)
    return result
