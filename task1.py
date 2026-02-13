def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary = line.split(",")
                    total += float(salary)
                    count += 1
                except ValueError:
                    continue

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)

with open("salary_file.txt", "w", encoding="utf-8") as f:
    f.write("Alex Korp,3000\n")
    f.write("Nikita Borisenko,2000\n")
    f.write("Sitarama Raju,1000\n")

total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")
