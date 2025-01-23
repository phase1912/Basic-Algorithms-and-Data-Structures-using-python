﻿import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (-priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return not bool(self.queue)

def convert_image(file_name, target_format):
    # Припустимо, що ця функція конвертує зображення (тут просто імітація)
    print(f"Конвертація {file_name} до {target_format} формату...")
    return f"{file_name.split('.')[0]}.{target_format}"

def main():
    pq = PriorityQueue()

    # Користувачі завантажують свої зображення
    pq.enqueue(("sample1.jpg", "png"), 1)  # Основний користувач
    pq.enqueue(("premium_sample.jpg", "bmp"), 10)  # Преміум-користувач
    pq.enqueue(("sample2.jpg", "tiff"), 1)  # Основний користувач

    while not pq.is_empty():
        file_name, target_format = pq.dequeue()
        output_file = convert_image(file_name, target_format)
        print(f"Зображення було успішно конвертовано і збережено як {output_file}!")

if __name__ == "__main__":
    main()

