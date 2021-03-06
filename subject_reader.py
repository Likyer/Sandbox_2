"""
CP-1404 Practical
Name:LIU YUHAO
"""

FILENAME = "subject_reader.txt"


def main():
    data = get_data()
    print(data)
    display_subject_detail(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print("parts".format(parts))  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
        print("----------")
    input_file.close()
    return data


def display_subject_detail(data):
    """print data"""
    for subject_detail in data:
        print("{0} is taught by {1:12} and has {2:0} students".format(*subject_detail))




main()
