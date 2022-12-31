import csv


def csv_distributor(file="C:/Users/Глеб/PycharmProjects/task2-2/v_year2.csv"):
    """
    Фильтрует файл от некорретных строк и создает словарь с вакансиями по годам
    """
    years_csv = {}
    with open(file, 'r', encoding='utf-8-sig') as File:
        reader = csv.reader(File)
        title = next(reader)
        title[0] = 'name'
        for data in list(reader):
            if len(title) == len(data) and '' not in data:
                year = data[title.index('published_at')][:4]
                if year not in years_csv.keys():
                    years_csv[year] = [data]
                else:
                    year_list = years_csv[year]
                    year_list.append(data)
                    years_csv[year] = year_list
    return years_csv, title


def create_csv_files(title: list, years_vacancies: dict):
    """
    Создаёт новые CSV-файлы в в папке CSVFiles

    Args:
        years_vacancies (dict): словарь со списками вакансий, привязанных к году
        title (list): cписок с заголовками
    """
    for year in years_vacancies:
        with open(f'CSVFiles/{year}.csv', 'w', encoding='utf-8-sig') as new_file:
            writer = csv.writer(new_file)
            writer.writerow(title)
            for row in years_vacancies[year]:
                writer.writerow(row)


csv_dict, title = csv_distributor()
create_csv_files(title, csv_dict)
