# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv

# Create an empty dictionary to record which students are in each course
students_per_course = {}
courses_per_student = {}

def calc_mean(values):
  
  return (sum(values) / len(values))

# Open the file and create a csv reader
f = open('enrollments.csv', 'rU')
reader = csv.reader(f)

def calc_median(values):
  values.sort()
  length = len(values)
  
  if length % 2 == 0:
    mid = values[length // 2]
    midup = values[length // 2 + 1]
    return (mid + midup) / 2
  else:
    return values[length // 2 + 1]

# Reader automatically iterates through the lines in the file
for line in reader:
    
    # csv reader automatically turns the line into a list of fields
    student_id = line[0]
    course_id = line[1]
    
    if course_id not in students_per_course:
        students_per_course[course_id] = []
        
    students_per_course[course_id].append(student_id)

    if student_id not in courses_per_student:
      courses_per_student[student_id] = []

    courses_per_student[student_id].append(course_id)
    
# Here's an example of how to iterate through the keys in a dictionary
# Print the students in each course
num_students = []
for course_id in students_per_course:
    student_list = students_per_course[course_id]
    num = 0
    for student in student_list:
      num += 1
    num_students.append(num)

length = len(num_students)
sum1 = 0
for i in num_students:
  sum1 += i
mean = sum1 / length

print("Mean:", mean)
print("Median:", calc_median(num_students))
# print(num_students)
  
      
# print(num_students)

# Create a new figure -- you must do this before calling a plotting function
plt.figure()

# Create a histogram with 15 bins
plt.hist(num_students, 20)

# Title and axis labels
plt.title('Students Per Course')
plt.xlabel('Class Size')
plt.ylabel('Number of Classes')

# Save the figure to a file
plt.savefig('Students Per Course.png', bbox_inches='tight')


fig = plt.figure()
# Create an axes instance
ax = fig.add_axes([0,0,1,1])
plt.title('Students Per Course')
plt.xlabel('Class Size')
plt.ylabel('Number of Classes')
# Create the boxplot
bp = ax.boxplot(num_students)
plt.savefig('Students Per Course plot.png', bbox_inches='tight')


num_of_same = []

# Get the key for the list of courses 
for student in courses_per_student:
  unique_id = []
  unique_id.append(student)
  # Get the course number and find the # of unique id
  for course_num in courses_per_student[student]:
    for other_student in students_per_course[course_num]:
      if other_student not in unique_id:
        unique_id.append(other_student)
  
    num_of_same.append(len(unique_id)-1)
yes = calc_mean(num_of_same)
print("Mean Connections: ", yes)