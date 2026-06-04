class StrWorkoutExercises:

    def __init__(self, workout_id: int = 0,
                 exercise_id: int = 0, sets: int = 0,
                 reps: str = '', weight: int = 0):
        self.workout_id: int = workout_id
        self.exercise_id: int = exercise_id
        self.sets: int = sets
        self.reps: str = reps
        self.weight: int = weight
        # self.execution_order: int = 0
