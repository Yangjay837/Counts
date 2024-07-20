
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
count_by = int(input("Enter the amount to count by: "))


if start_num > end_num:
    print("Error: Starting number cannot be greater than ending number.")
elif count_by <= 0:
    print("Error: Count increment must be a positive integer.")
else:
   
    for i in range(start_num, end_num + 1, count_by):
        print(i)