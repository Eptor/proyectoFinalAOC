import subprocess
import os

count = int(input("Longitud (Minimo 10 caracteres): "))
final_count = count
if os.path.isfile("final.txt"):
    os.remove("final.txt")

for _ in range(0, count+1, 10):
    print(count)
    subprocess.run("prueba_randomizer2.exe", capture_output=True)
    with open("data.txt", "r") as rand:
        raw = rand.read()
        raw = raw.split(",")
        ints = [int(x.replace("\x00", "")) for x in raw[:-1]]
        chars = [chr(i) for i in ints]
    

