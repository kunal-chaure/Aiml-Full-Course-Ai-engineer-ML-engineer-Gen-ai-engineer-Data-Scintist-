data = True
with open("info.txt","r") as f:
    while data:
        data  = f.readline()
        if ("year"  in data):
              print("word found")
              break
        print(data)