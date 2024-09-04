f = open("weather.txt", "r")
weather = f.readlines()
f.close()
for i in range(len(weather)):
    weather[i] = weather[i].replace("\n", "")
    weather[i] = weather[i].replace(";", "")
    weather[i] = weather[i].replace(".", "")
    weather[i] = weather[i].replace("degrees", "").strip()

degree = []
for line in weather:
    parts = line.split()
    degree.append(int(parts[-1]))
max = degree[0]
min = degree[0]
for i in range(1,len(degree)):
    if degree[i] > max:
        max = degree[i]
    if degree[i] < min:
        min = degree[i]
        
print(f"{min} {max}")