
test_input = 1234
su = 0
while test_input > 0:
    su = su + test_input % 10
    test_input = test_input // 10
print(su)