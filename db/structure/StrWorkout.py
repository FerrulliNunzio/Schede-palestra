class StrWorkout:
    def __init__(self, id_workout: int = 0, id_training_plan: int = 0, name: str ='', day_week: str = ''):
        self.id_workout: int = id_workout
        self.id_training_plan: int = id_training_plan
        self.name: str = name
        self.day_week: str = day_week