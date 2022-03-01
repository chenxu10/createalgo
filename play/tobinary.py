def to_binary(n):
    t = n
    ans = []
    while t > 0:
        ans = [t % 2] + ans
        t = t // 2
    return ans
 
if __name__ == '__main__':
    print(to_binary(13))