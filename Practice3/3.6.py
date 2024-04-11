import matplotlib.pyplot as plt
import csv
import datetime
import pandas as pd


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# Сообщения, присланные в ЦАП.
# id, task, variant, group, time
messages = load_csv('data/messages.csv')

# Результаты проверок сообщений, присланных в ЦАП.
# id, message, time, status
checks = load_csv('data/checks.csv')

# Состояния задач ЦАП.
# task, variant, group, time, status, achievements
statuses = load_csv('data/statuses.csv')

# Таблица соответствия номеров групп и их названий.
# id, title
groups = load_csv('data/groups.csv')

# О статусах см. https://github.com/kispython-ru/dta/blob/main/webapp/models.py#L44-L50

data = list(filter(lambda x: x[4] == "2", statuses))
data = list(map(lambda x: groups[int(x[2])][1], data))
data = pd.Series(data).value_counts()

plt.figure(figsize=(20, 8))
plt.bar(data.index, data)
plt.ylabel("Правильные решения")
plt.xlabel("Группа")
plt.xticks(rotation=90)
plt.show()