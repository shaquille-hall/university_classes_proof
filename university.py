from college import College

class University:
	name = ""
	colleges = []

	def __init__(self, university_name, colleges):
		self.name = university_name
		self.colleges = colleges

	def addCollege(self, new_college: College):
		self.colleges.append(new_college)

	def removeCollege(self, collegeToRemove: College):
		for college in self.colleges:
			if college.name == collegeToRemove.name:
				self.colleges.remove(college)

	def printNameHierarchy(self):
		print(self.name)
		for college in self.colleges:
			print("\t" + college.name)
			for department in college.departments:
				print("\t\t" + department.name)

	def calculateTotalPersonnel(self):
		total = 0
		for college in self.colleges:
			total += college.getCollegeTotalPersonnel()
		return total

	def calculateAvgStudentGPA(self):
		total_students = 0
		total_gpa = 0
		for college in self.colleges:
			total_students += college.getTotalStudents()
			total_gpa += college.getTotalGpa()

		return total_gpa / total_students

	
