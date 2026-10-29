import sys
from collections import Counter


def parse_log_line(line: str) -> dict:
    date, time, level, message = line.split(" ", 3)
    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            try:
                logs.append(parse_log_line(line))
            except ValueError:
                print(f"Некоректний рядок пропущено: {line}")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return Counter(levels)


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу: python main.py <шлях> [рівень]")
        return

    file_path = sys.argv[1]

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
