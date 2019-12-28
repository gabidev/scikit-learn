import random

def bmi_func(height, weight):
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5: return "저체중"
    if bmi < 25: return "정상"
    return "비만"

fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\n")

cnt = {"저체중":0, "정상":0, "비만":0}

for i in range(10000):
    h = random.randint(120, 200)
    w = random.randint(35, 90)
    label = bmi_func(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\n".format(h, w, label))

fp.close()
print("ok, ", cnt)