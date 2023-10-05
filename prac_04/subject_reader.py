"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data_number = get_data()
    subject_details(data_number)
    print(data_number)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_number=[]
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_number.append(parts)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()
    return data_number

def subject_details(data_number):
    for subject_name in data_number:
        subject, lecturer, num_student = subject_name
        print(f"{subject} taught by{lecturer}and has{num_student} student")


main()