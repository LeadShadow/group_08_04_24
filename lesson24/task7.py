# Клас Timer
# Створіть клас Timer, який вимірює час виконання блока коду.
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        duration = end_time - self.start_time
        print(f'Time taken: {duration:.4f} seconds')


with Timer() as timer:
    total = sum(range(100_000_000))

