import datetime

week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
          "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
people_in_weeks = [0, 0, 0, 0, 0, 0, 0]
people_in_months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def main():
    processed_data = data_handler("data.txt")

    calculate_people(processed_data)

    output_data()

    print(f"Месяц с большим кол-вом поситителей: {months[find_max_index(people_in_months)]}")
    print(f"Месяц с меньшим кол-вом поситителей(не нулевым): {months[find_min_index(people_in_months)]}")
    print(f"День недели с большим кол-вом поситителей: {week_days[find_max_index(people_in_weeks)]}")
    print(f"День недели с меньшим кол-вом поситителей: {week_days[find_min_index(people_in_weeks)]}")


def calculate_people(processed_data: list):
    for data in processed_data:
        d = data.split(",")

        current_date = datetime.datetime.strptime(d[0], "%Y-%m-%d")

        people_in_weeks[current_date.date().weekday()] += int(d[1])
        people_in_months[current_date.month-1] += int(d[1])


def output_data():
    print("!Вся информация!")

    for i in range(0, len(months), 1):
        print(f"Количество песещений в {months[i]}: {people_in_months[i]}")

    for i in range(0, len(week_days), 1):
        print(f"Количество песещений в {week_days[i]}: {people_in_weeks[i]}")

    print("-----")


def data_handler(file_name: str) -> list:
    with open(file_name, "r") as file:
        data = file.read()
    return data.split("\n")


def find_max_index(nums: list) -> int:
    if not nums:
        raise ValueError("")

    max_number = nums[0]
    index_number = 0

    for i in range(1, len(nums), 1):
        if nums[i] > max_number:
            max_number = nums[i]
            index_number = i

    return index_number


def find_min_index(nums: list) -> int:
    if not nums:
        raise ValueError("")

    max_number = nums[0]
    index_number = 0

    for i in range(1, len(nums), 1):
        if nums[i] != 0:
            if nums[i] < max_number:
                max_number = nums[i]
                index_number = i

    return index_number


main()