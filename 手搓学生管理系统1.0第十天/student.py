from settings import PASS_SCORE
class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores
        
    def calculate_average(self):
        return sum(self.scores)/len(self.scores)
    
    def change_scores(self,new_scores):
        self.scores=new_scores
        
    def show_info(self):
        average=self.calculate_average()
        if average<PASS_SCORE:
            status="不合格"
        else:
            status="合格"
        print(f"名字是{self.name},各科成绩是{self.scores},平均分是{average},评价是{status}")
        