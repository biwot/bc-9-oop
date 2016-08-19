
class Student(object):
	cc_codes_={
			'KE': 'KENYA',
			'UG': 'UGANDA',
			'NG': 'NIGERIA',
			'SD': 'SUDAN'
		}
	count= 0
	my_register= {}
	student_details=[]

	def __init__(self, lname, fname, cc= "KE"):

		self.fname= fname
		self.lname= lname
		self.cc= cc
		Student.count+=1
		self.id= Student.count

	def attend_class(self, **vars):

		self.date= vars.setdefault("date", datetime.now())
		self.loc= vars.setdefault('loc', 'Hogwarts')
		self.teacher= vars.setdefault('teacher', 'alex')
		#append students to a list/dictionary here
		student_details.extend(self.fname, self.lname, self.country)
		my_register.update({self.id: student_details})
	
	def check_prescence(self, attended_date):
		self.attended_date= self.date
		absentees= []
		#loop through the dict/list appended to
		for k,v in Student.my_register:
			for info in v:
				if not self.date==attended_date:
					absentees.extend(k)
			return absentees


		

				




