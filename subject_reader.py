"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load data from file and display subject details."""
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the newline character at the end of the line
        parts = line.split(',')  # Split the line into a list of its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        data.append(parts)  # Add the parts (as a list) to the data list
    input_file.close()  # Close the file after reading all the lines
    return data


def display_subject_details(data):
    """Display subject details in a formatted manner."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
