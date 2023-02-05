print("Enter words separated by Hyphens : ")
l = [w for w in input().split("-")]
l.sort()
print('-'.join(l))