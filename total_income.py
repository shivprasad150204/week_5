def main():
    # Task 1: Display income report using enumerate
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)

    # Task 2: Extend list_exercises to accept numbers until a negative number is entered
    numbers = []
    count = 1
    
    while True:
        number = int(input(f"Number {count}: "))
        if number < 0:
            break
        numbers.append(number)
        count += 1

    if numbers:
        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
    else:
        print("No numbers were entered.")

    # Task 3: Program to find and print repeated strings
    strings = []
    string_count = {}

    while True:
        string = input("Enter a string (or press Enter to finish): ")
        if string == "":
            break
        strings.append(string)
        if string in string_count:
            string_count[string] += 1
        else:
            string_count[string] = 1

    repeated_strings = [string for string, count in string_count.items() if count > 1]
    
    if repeated_strings:
        print("Strings repeated:", ", ".join(repeated_strings))
    else:
        print("No repeated strings entered.")

    # Task 4: Function to add elements of two lists memberwise
    def add_memberwise(list1, list2):
        length = max(len(list1), len(list2))
        result = []
        
        for i in range(length):
            value1 = list1[i] if i < len(list1) else 0
            value2 = list2[i] if i < len(list2) else 0
            result.append(value1 + value2)

        return result

    # Test cases for add_memberwise function
    print(add_memberwise([1, 2, 3], [4, 5, 6]))  # Output: [5, 7, 9]
    print(add_memberwise([1, 2, 3], [1, 2, 3, 4]))  # Output: [2, 4, 6, 4]

def print_report(incomes):
    """Print income report based on incomes list using enumerate."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

if __name__ == "__main__":
    main()
