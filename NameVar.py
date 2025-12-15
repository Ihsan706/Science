first = int(input("say the first number:"))
end = int(input("sey where it ends:"))
extra_data = input("anything to add:")

for i in range(end):
    print(f"{first + i}{extra_data}")
