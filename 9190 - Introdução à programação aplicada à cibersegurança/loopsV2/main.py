i = 0

while True:
    print(i)

    if i == 3234:
        break

    i += 1




print("Fim so while")


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lst:

    if i == 5:
        print("i == 5")
        break

    if i % 2 == 0:
        print("par - vai para o i segiunte")
        continue



    print(i)

print("Fim do for")