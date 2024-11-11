test_input = 1234

ans = 0
while test_input > 0:
    ans += test_input % 10
    test_input //= 10

print(ans)
