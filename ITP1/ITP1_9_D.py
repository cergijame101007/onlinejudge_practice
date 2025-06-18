s = input()
q = int(input())
command_list = []
for i in range(q):
    command_list = input().split()
    op = command_list[0]
    a = int(command_list[1])
    b = int(command_list[2])
    if op == "replace":
        s = s[:a] + command_list[3] + s[b+1:]
    elif op == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif op == "print":
        print(s[a:b+1])