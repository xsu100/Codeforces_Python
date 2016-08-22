s = ""
for _ in range(input()):
    s += raw_input()
print (s.count("+") - s.count("-")) / 2

#print sum([-1,1][raw_input()[1]=='+'] for _ in [0]*input())
