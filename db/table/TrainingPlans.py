from db.structure.StrTrainingPlans import StrTrainingPlans
from db.table.TableOperation import TableOperation
import pandas as pd


class TrainingPlans(TableOperation):
    def __init__(self):
        self.__training_plans: list = []
        try:
            training_plans = pd.read_csv("TrainingPlans.csv")
            lst = training_plans.values.tolist()
            for item in lst:
                self.__training_plans.append(StrTrainingPlans(item[0], item[1], item[2], item[3], item[4], item[5]))
        except FileNotFoundError:
            self.__training_plans = []

    def get(self):
        return self.__training_plans

    def add_training_plans(self, training_plans: StrTrainingPlans):
        if len(self.__training_plans) <= 0:
            training_plans.TrainingPlansId = 1
            self.__training_plans.append(training_plans)
            to_save: list = []
            to_save.append([
                'TrainingPlansId',
                'UserId',
                'Workout',
                'Name',
                'Goal',
                'Duration',
            ])
            for item in self.__training_plans:
                to_save.append([item.TrainingPlansId,
                                item.UserId,
                                item.Workout,
                                item.Name,
                                item.Goal,
                                item.Duration])
            self.save_table("TrainingPlans.csv", to_save)
        else:
            training_plans.TrainingPlansId = self.find_new_primary_key()
            self.__training_plans.append(training_plans)
            to_save: list = []
            to_save.append([
                'TrainingPlansId',
                'UserId',
                'Workout',
                'Name',
                'Goal',
                'Duration',
            ])
            for item in self.__training_plans:
                to_save.append([item.TrainingPlansId,
                                item.UserId,
                                item.Workout,
                                item.Name,
                                item.Goal,
                                item.Duration])
            self.save_table("TrainingPlans.csv", to_save)

    def size(self) -> int:
        return len(self.__training_plans)

    def find_new_primary_key(self):
        maxid: str = self.__training_plans[0].TrainingPlansId
        for i in range(len(self.__training_plans)):
            if maxid < self.__training_plans[i].TrainingPlansId:
                maxid = self.__training_plans[i].TrainingPlansId
        return maxid + 1
