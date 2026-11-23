from settings import PASS_SCORE
from student import Student
def show_report(manager):
    if not manager.students:
        print("暂无学生,无法生成班级报告")
        return
    
    ranking=list(manager.students.values())
    ranking.sort(key=lambda student: student.calculate_average(), reverse=True)
    
    total=0
    passed=0
    
    print("\n======= 班级成绩排名 =======")
    for index,student in enumerate(ranking,start=1):
        average=student.calculate_average()
        total+=average
        if average>=PASS_SCORE:
            passed+=1
        print(f"第{index}名是{student.name},平均分是{average}")
        
    class_average=total/len(ranking)
    print(f"班级平均分是{class_average},及格人数是{passed},班级人数是{len(ranking)}")
    
