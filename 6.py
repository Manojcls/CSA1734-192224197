class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.location = 'A'  
        self.performance_score = 0
    def sense(self):
        return self.environment[self.location]
    def act(self, action):
        if action == 'CLEAN':
            if self.environment[self.location] == 'DIRTY':
                self.environment[self.location] = 'CLEAN'
                self.performance_score += 1
        elif action == 'RIGHT':
            self.location = 'B'
        elif action == 'LEFT':
            self.location = 'A'
    def run(self):
        for _ in range(5):  
            if self.sense() == 'DIRTY':
                self.act('CLEAN')
            elif self.location == 'A':
                self.act('RIGHT')
            elif self.location == 'B':
                self.act('LEFT')
        return self.performance_score
environment = {
    'A': 'DIRTY',
    'B': 'DIRTY'
}
vacuum_cleaner = VacuumCleaner(environment)
score = vacuum_cleaner.run()
print("Final Environment State:", environment)
print("Performance Score:", score)
