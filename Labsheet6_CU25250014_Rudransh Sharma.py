# LAB 6 - QUESTION 1
# 3 Sum Problem
def three_sum(arr, target):

    n = len(arr)

    for i in range(n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == target:

                    print("Triplet found:")
                    print(arr[i], "+", arr[j], "+", arr[k], "=", target)
                    return

    print("No triplet found.")

arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter target sum: "))

three_sum(arr, target)


# LAB 6 - QUESTION 2
# Fibonacci Series using recursion
def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")

# LAB 6 - QUESTION 3
# Tower of Hanoi using recursion
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)

n = int(input("Enter number of disks: "))
print("\nSteps to solve Tower of Hanoi:")
tower_of_hanoi(n, "A", "B", "C")
