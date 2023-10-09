people = set(input("Enter a list of names: ").split(", "))

for i in range(len(people)):
    x = people.pop()

    print(x, "was chosen!")
    #[print(j, end=" ") for j in people]