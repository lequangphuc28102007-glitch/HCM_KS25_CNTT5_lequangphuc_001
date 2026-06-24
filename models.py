from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, id, name, speed_score, technique_score, goal_score):
        self.id = id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score

        self.average_score = 0
        self.performance_type = ""

    def calculate_average(self):
        self.average_score = self.speed_score * 0.3 + self.technique_score * 0.4 + self.goal_score * 0.3

    def classify_performance(self):
        if self.average_score < 5.0:
            self.performance = "dự bị yếu"

        elif self.average_score < 6.5:
            self.performance = "trung bình"
        
        elif self.average_score < 8.0:
            self.performance = "tốt"

        else:
            self.performance = "ngôi sao"

    def update_status_player(self):
        self.calculate_average()
        self.classify_performance()

        