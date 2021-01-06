n = int(input())
phonelist = dict()
for i in range(n):
    user = input().strip().split()
    phonelist[user[0]] = user[1]
for i in range(n):
    while True:
        try:
            ask = input()
            if ask in phonelist:
                print(f"{ask}={phonelist[ask]}")
            else:
                print("Not found")  # RUNTIME Error at case 1
        except:  # break when exception in reading EOF
            break

