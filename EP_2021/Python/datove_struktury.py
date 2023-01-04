pole = [12, "text", 13.2, [1, 2]]

prvek = pole[0]
prvek = pole[3][1]

print(prvek)


posledni = pole[len(pole) - 1]

print(posledni)
print(pole[-3])
print(pole[1:3])
print(pole[::3])

pole.append("co chci přidat")
pole.pop(1)
print(pole)


tup = (1, "text", 3.14)
print(tup[-1])

# tup[0] = 5 # vyhodí chybu

st = {1, 2, 3, "text"}
print(st)

st.add(2)
print(st)

dic = {
    "jedna": 1,
    "dva": 2,
    "pole": [3.14, 5],
    "set": {1, 2, 3, "text"},
    "dic": {
        "slovo": "text"
    }
}

print(dic)
print(dic["jedna"])
print(dic["pole"][0])

print(dic.keys())
print(dic.values())


text = "ukázkový text"
print(text.split("t"))


a = 15
text_2 = "proměnná 'a' má hodnotu {ukazka}".format(ukazka=a)
print(text_2)

text_3 = f"proměnná 'text' má hodnotu {text} \ntext \ttabulátor"
print(text_3)
print(len(text_3))

print(text_3[2])

text_4 = ".".join(["slovo", "druhé"])
print(text_4)

text_5 = "        ahoj        "
print(text_5.strip())

pole = [12, "text", 13.2, [1, 2]]

if 12 in pole:
    print("ano")


x = [12, "text", 13.2, [1, 2]]
y = x
print(x is y)
x.pop(1)
print(y)


x = [12, "text", 13.2, [1, 2]]
y = [12, "text", 13.2, [1, 2]]
print(x is y)