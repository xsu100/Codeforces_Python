n,k = map(int, raw_input().split())
a = map(int, raw_input().split())
print sum(i>=max(1,a[k-1]) for i in a)
