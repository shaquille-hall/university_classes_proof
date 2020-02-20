from student import Student
from staff import Staff
from faculty import Faculty


class Department:
	name = ""
	students = []
	faculty = []
	staff = []

	def __init__(self, name, students, faculty, staff):
		self.name = name
		self.students = students
		self.faculty = faculty
		self.staff = staff

	def addStudent(self, student: Student):
		self.students.append(student)

	def addFaculty(self, faculty: Faculty):
		self.faculty.append(student)

	def addStaff(self, staff: Staff):
		self.staff.append(staff)

	def removeStudent(self, studentToRemove: Student):
		for student in self.students:
			if student.id == studentToRemove.id:
				self.students.remove(student)	

	def removeFaculty(self, facultyToRemove: Faculty):
		for faculty in self.faculty:
			if faculty.id == facultyToRemove.id:
				self.faculty.remove(faculty)

	def removeStaff(self, staffToRemove: Staff):
		for staff in self.staff:
			if staff.id == staffToRemove.id:
				self.staff.remove(staff)

	def getDepartmentTotalPersonnel(self):
		return(len(self.students) + len(self.faculty) + len(self.staff))

	def getTotalGpa(self):
		total_gpa = 0;
		for student in self.students:
			total_gpa += student.gpa

		return total_gpa
			
