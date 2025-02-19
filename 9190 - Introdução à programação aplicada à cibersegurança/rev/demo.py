tp = ("Gonçalo", 38, True)


print(tp)
print(tp[0])

tp_l = list(tp)
#print(tp_l)
tp_l[1] = 39
tp = tuple(tp_l)

print(tp)