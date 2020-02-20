from university import University
from college import College
from department import Department
from student import Student
from faculty import Faculty
from staff import Staff 
import testdata

colleges = []

def initTestData():
	engineering_students = []
	engineering_faculty = []
	engineering_staff = []
	business_students = []
	business_faculty = []
	business_staff = []
	social_science_students = []
	social_science_faculty = []
	social_science_staff = []

	engineering_departments = []
	for department_name in testdata.ENGINEERING_DEPARTMENTS:
		engineering_students = [Student(s[0], s[1], s[2], s[3], s[4], s[5], s[6]) for s in testdata.ENGINEERING_STUDENTS]		
		engineering_faculty = [Faculty(f[0], f[1], f[2], f[3], f[4], f[5], f[6]) for f in testdata.ENGINEERING_FACULTY]		
		engineering_staff = [Staff(stf[0], stf[1], stf[2], stf[3], stf[4], stf[5], stf[6]) for stf in testdata.ENGINEERING_STAFF]
		engineering_departments.append(Department(department_name, engineering_students, engineering_faculty, engineering_staff))				
	colleges.append(College(testdata.COLLEGE_OF_ENGINEERING, engineering_departments)) 

	business_departments = []
	for department_name in testdata.BUSINESS_DEPARTMENTS:
		business_students = [Student(s[0], s[1], s[2], s[3], s[4], s[5], s[6]) for s in testdata.BUSINESS_STUDENTS]		
		business_faculty = [Faculty(f[0], f[1], f[2], f[3], f[4], f[5], f[6]) for f in testdata.BUSINESS_FACULTY]		
		business_staff = [Staff(stf[0], stf[1], stf[2], stf[3], stf[4], stf[5], stf[6]) for stf in testdata.BUSINESS_STAFF]
		business_departments.append(Department(department_name, business_students, business_faculty, business_staff))				
	colleges.append(College(testdata.COLLEGE_OF_BUSINESS, business_departments)) 
			
	social_science_departments = []
	for department_name in testdata.SOCIAL_SCIENCE_DEPARTMENTS:
		social_science_students = [Student(s[0], s[1], s[2], s[3], s[4], s[5], s[6]) for s in testdata.SOCIAL_SCIENCE_STUDENTS]		
		social_science_faculty = [Faculty(f[0], f[1], f[2], f[3], f[4], f[5], f[6]) for f in testdata.SOCIAL_SCIENCE_FACULTY]		
		social_science_staff = [Staff(stf[0], stf[1], stf[2], stf[3], stf[4], stf[5], stf[6]) for stf in testdata.SOCIAL_SCIENCE_STAFF]
		social_science_departments.append(Department(department_name, social_science_students, social_science_faculty, social_science_staff))				
	colleges.append(College(testdata.COLLEGE_OF_SOCIAL_SCIENCE, social_science_departments)) 
	

def main(): 
	initTestData()
	university = University("Drexel University", colleges)

	university.printNameHierarchy()
	print("Total University Personnel = ", university.calculateTotalPersonnel())
	print("Average Student GPA = ", university.calculateAvgStudentGPA())

	college = College("College of Engineering", colleges[0].departments[0])	
	university.removeCollege(college)


main()
