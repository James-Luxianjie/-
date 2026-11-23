from student_manager import StudentManager
from report import show_report
from settings import MIN_SCORE, MAX_SCORE


def read_scores():
    # 例如输入 80,90,85，转换成 [80, 90, 85]
    text = input("请输入成绩(用英文逗号分隔,例如80,90,85):")
    scores = []

    try:
        for part in text.split(","):
            score = int(part.strip())
            if score < MIN_SCORE or score > MAX_SCORE:
                print("成绩必须在0到100之间")
                return None
            scores.append(score)
    except ValueError:
        print("输入格式有误，请输入整数并用英文逗号分隔")
        return None

    return scores


def show_menu():
    print("\n======= 学生成绩管理系统 =======")
    print("1. 查看全部学生")
    print("2. 添加学生")
    print("3. 修改学生成绩")
    print("4. 删除学生")
    print("5. 查看班级报告")
    print("0. 退出程序")
    
    
def main():
    manager=StudentManager()
    manager.add_students("Alice",[80,90,100])
    manager.add_students("Bob",[60,70,80])
    manager.add_students("原神",[10,20,30])
    
    while True:
        show_menu()
        choice=input("请输入数字执行操作").strip()
        if choice=="1":
            manager.manager_show_info()
            
        elif choice=="2":
            name=input("请输入学生姓名").strip()
            if not name:
                print("名字不能为空")
                
            else:
                scores=read_scores()
                if scores is not None:
                    if manager.add_students(name, scores):
                        print("添加成功")
                    else:
                        print("该学生已经存在")
        elif choice=="3":
            name=input("请输入要修改的学生姓名").strip()
            if name not in manager.students:
                print("找不到这个学生")
            else:
                scores=read_scores()
                if scores is not None:
                    manager.change_students(name,scores)
                    print("更改姓名成功")
        elif choice=="4":
            name=input("请输入要删除的学生").strip()
            if name not in manager.students:
                print("查无此人")
            else:
                manager.del_students(name)
                print("已经删除此人")
                
        elif choice=="5":
            show_report(manager)
            
        elif choice=="0":
            print("再见！")
            break
        
        else:
            print("请输入有效数字")
            
        input("\n按 Enter 返回菜单...")#暂停程序，**等待用户按下回车键之后，才继续往下运行（回到菜单页面）**

if __name__=="__main__":
    main()
            