"""
The program would like to display the number of grades, the average 
grade, and the percentage of grades that are above the average grade
by accessing a file named Final.txt, which contains student grades
on the final exam. The program will be using two function. 

The file will be open to get the information and closed after the 
information have been extracted.
The first function named main will start the application. 
The second function named calculate percent above average will 
calculate the percentage of grades that are above the average grade. 
"""

"""
Open file Final.txt in read mode 
grades = [line.rstrip() for line in infile] 
close the file 

main():

    average_grade = sum(grades)/len(grades)

def calculate_percent_above_average(Final, average):

    calculate percent above average 

print number of grades 
print average grade 
print percentage of grades above average 2 decimals 

run main function
"""

def main():
    infile = open("Final.txt", 'r')
    grades = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(grades)):
        grades[i] = int(grades[i])
    average = sum(grades)/len(grades)
    num = 0
    for grade in grades:
        if grade > average:
            num += 1
    print("Number of grades:", len(grades)) 
    print("Average grade:", average) 
    print("Percentage of grades above average: {0:.2f}%" .format(100 * num / len(grades)))

main()