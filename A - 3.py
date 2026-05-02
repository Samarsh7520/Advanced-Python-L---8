def ONsqauretime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
            iteration += 1
        print("")
    print("\n When n is ",n,"Iterations = ",iteration,"\n")

ONsqauretime(5)
ONsqauretime(4)
ONsqauretime(3)

print("\nWith every 'n' the time taken is equals to n^2")
print("0(n^2)")