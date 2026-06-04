from db.exception.GeneralErrorException import GeneralErrorException


class StrTrainingPlans:

    def __init__(self, training_plans_id: int = 0, user_id: int = 0, workout: int = 0, name: str = '', goal: str = '', duration: int = 0):
        self.__training_plans_id: int = training_plans_id   #PrimaryKey
        self.__user_id: int = user_id                       #ForeignKey
        self.__workout: int = workout
        self.__name: str = name
        self.__goal: str = goal
        self.__duration: int = duration

    @property
    def TrainingPlansId(self) -> str:
        return self.__training_plans_id

    @TrainingPlansId.setter
    def TrainingPlansId(self, training_plans_id: int):
        if training_plans_id <= 0:
            raise GeneralErrorException()
        self.__training_plans_id = training_plans_id

    @property
    def UserId(self) -> str:
        return self.__user_id

    @UserId.setter
    def UserId(self, user_id: str):
        if len(user_id) <= 0:
            raise GeneralErrorException()
        if len(user_id) > 8:
            raise GeneralErrorException()
        self.__user_id = user_id

    @property
    def Workout(self) -> int:
        return self.__workout

    @Workout.setter
    def Workout(self, workout: int):
        self.__workout = workout

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, name: str):
        self.__name = name

    @property
    def Goal(self) -> str:
        return self.__goal

    @Goal.setter
    def Goal(self, goal: str):
        self.__goal = goal

    @property
    def Duration(self) -> int:
        return self.__duration

    @Duration.setter
    def Duration(self, duration: int):
        self.__duration = duration
