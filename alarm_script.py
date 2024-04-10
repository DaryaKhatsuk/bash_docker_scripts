import psutil
import requests
import time


class MemoryMonitor:
    def __init__(self, alarm_api_url, memory_threshold_percent):
        self.ALARM_API_URL = alarm_api_url
        self.MEMORY_THRESHOLD_PERCENT = memory_threshold_percent

    def send_alarm(self):
        # Отправка HTTP-запроса на API для генерации тревоги
        response = requests.post(self.ALARM_API_URL)
        if response.status_code == 200:
            print("Alarm sent successfully!")
        else:
            print("Failed to send alarm.")

    def monitor_memory_usage(self):
        while True:
            # Получаем информацию о потреблении памяти
            memory_percent = psutil.virtual_memory().percent
            print(memory_percent)
            # Проверяем, превышает ли потребление памяти пороговое значение
            if memory_percent > self.MEMORY_THRESHOLD_PERCENT:
                print(f"Memory usage exceeded threshold ({memory_percent}%). Sending alarm...")
                self.send_alarm()

            # Задержка перед следующей проверкой
            time.sleep(60)  # Проверяем каждую минуту


if __name__ == "__main__":
    monitor = MemoryMonitor("https://example.com/send_alarm", 90)
    monitor.monitor_memory_usage()
