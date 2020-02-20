from department import Department

class College:
	name = ""
	departments = []
	

	def __init__(self, name, departments):
		self.name = name
		self.departments = departments

	
	def addDepartment(self, new_department: Department):
		self.departments.append(new_department)
	
	def removeDepartment(self, departmentToRemove: Department):
		for department in self.departments:
			if department.name == departmentToRemove.name:
				self.departments.remove(department)
	
	def printDepartments(self):
		for department in self.departments:
			print(department.name)

	def getCollegeTotalPersonnel(self):
		total = 0
		for department in self.departments:
			total += department.getDepartmentTotalPersonnel()

		return total

	def getTotalStudents(self):
		total_students = 0
		for department in self.departments:
			total_students += len(department.students)
		return total_students
	
	def getTotalGpa(self):
		total_gpa = 0
		for department in self.departments:
			total_gpa += department.getTotalGpa()
		return total_gpa
