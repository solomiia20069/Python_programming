class Counter:
    def __init__(self, current=1, min_min=0, max_max=10):
        self.current = current
        self.min_min = min_min
        self.max_max = max_max

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        self.max_max = max_max

    def set_min(self, min_min):
        self.min_min = min_min

    def step_up(self):
        if self.current >= self.max_max:
            raise ValueError("Достигнут максимум")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_min:
            raise ValueError("Достигнут минимум")
        self.current -= 1

    def get_current(self):
        return self.current

# Example usage and test cases
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'
