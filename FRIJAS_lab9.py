def print_right_angled_triangle():
    # Prompt the user for the number of rows
    rows = int(input("Enter the number of rows for the triangle: "))
    
    # Use a for loop to print the triangle
    for i in range(1, rows + 1):
        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=' ')  # Print numbers in the same line
        print()  # Move to the next line after each row

# Run the triangle printing function
print_right_angled_triangle()