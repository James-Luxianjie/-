from student import Student
class StudentManager:
    def __init__(self):
        self.students={}#一个字典里面可以包含多个学生及其对应的成绩
        
    def add_students(self,name,scores):
        if name in self.students:
            return False
        self.students[name]=Student(name,scores)# self.students[name]中的name是键名
        return True
    
    def change_students(self,name,scores):
        if name not in self.students:
            return False
        self.students[name].change_scores(scores)
        return True
    
    def del_students(self,name):
        if name not in self.students:
            return False
        del self.students[name]
        return True
    
    def manager_show_info(self):
        if not self.students:
            print("暂无学生")
            return
        for student in self.students.values():
            student.show_info()
            
    