"""
The program would like to display the number of grades, the average 
grade, and the percentage of grades that are above the average grade
by accessing a file named Final.txt, which contains student grades
on the final exam. The program will be using two function. 

The file will be open to get the information and closed after the 
information have been extracted.
The first function named main will start the application. 
The average grade will be calculate within the main function. 
The second function named calculate percent above average will 
calculate the percentage of grades that are above the average grade. 
"""
"""
open file Final.txt in read mode
read the file and print out the grades 
close the file
 
main(): 
    set grade equal to a list of integers 

 
calculate_percent_above_average(): 

 
run main function
"""

#calculate_percent_above_average function
def calculate_percent_above_average(ll,avg):
        count=0
        for a in ll:
                if(a>avg):
                        cnt+=1
        return ((count/len(ll))*100)

#main function

if __name__ == "__main__":
        #opening python file
        #Here file name is abc.py you can change it 
        #as per your file name
        infile = open("Final.txt", "r")
        #spliting element by enter
        l=infile.read().split("\n")
        ll = []
        for a in l:
                if(a!=''):
                        ll.append(int(a))
        #ll is list of integers
        #printing number of grades
        print("Number of grades : ",len(ll))

        #lets calculate average grade
        avg=0
        for a in ll:
                avg+=a
        avg=avg/len(ll)
        print("Average of grades : ",avg)
        print("Percentage of grades above average: ",calculate_percent_above_average(ll,avg),"%")