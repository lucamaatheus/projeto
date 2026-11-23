temperatura = []
meses = ["january","february","march","april","may","june","july","agoust","september","october","november","december"]
for x in range (11):
  temp = float(input("digite a temperatura: "))
  temperatura.append(temp)
media = sum(temperatura)/11
print("media atual: ", round(media, 2))

for x in range(11):
    if temperatura[x]>media:
        print(meses[x], temperatura[x])

