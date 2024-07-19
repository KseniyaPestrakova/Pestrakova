'''Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv
. Функция должна вычислить средний возраст мужчин и женщин отдельно и вернуть результат
 в виде словаря в формате JSON.'''

# import pandas as pd
# import json
# import csv
#
# def avg_age_by_gender():
#     df = pd.read_csv("..\\data\\titanic.csv")
#     avg_age_male = df[df['Sex'] == 'male']['Age'].mean()
#     avg_age_female = df[df['Sex'] == 'female']['Age'].mean()
#     result_dict = {'Мужчины': avg_age_male, 'Женщины': avg_age_female}
#     return json.dumps(result_dict)
#
# print(avg_age_by_gender())





#Тест:

# import json
# import pytest
# import pandas as pd
#
# @pytest.fixture
# def titanic_df():
#     sample_dict = {'PassengerId': [1, 2, 3, 4, 5],
#                    'Survived': [0, 1, 1, 1, 0],
#                    'Pclass': [3, 1, 3, 1, 3],
#                    'Name': ['name1', 'name2', 'name3', 'name4', 'name5'],
#                    'Sex': ['male', 'female', 'female', 'female', 'male'],
#                    'Age': [22.0, 38.0, 26.0, 35.0, 35.0],
#                    'SibSp': [1, 1, 0, 1, 0],
#                    'Parch': [0, 0, 0, 0, 0],
#                    'Ticket': ['tic1', 'tic2', 'tic3', 'tic4', 'tic5'],
#                    'Fare': [7.3, 71.3, 7.9, 53.1, 8.1],
#                    'Cabin': [None, 'C85', None, 'C123', None],
#                    'Embarked': ['S', 'C', 'S', 'S', 'S']}
#     return pd.DataFrame(sample_dict)
#
# def test_avg_age_by_gender(titanic_df):
#     expected_result = {'Мужчины': 28.5, 'Женщины': 29.7}
#     assert avg_age_by_gender(titanic_df) == json.dumps(expected_result)


'''Напишите функцию, которая должна отфильтровать DataFrame,
чтобы в нем остались только мужчины старше 50 лет или женщины младше 30 лет.
Функция должна вернуть отфильтрованный DataFrame в формате JSON.'''

# import pandas as pd
# import json
#
# def filter_passengers(df):
#
#     result_df = df[((df['Sex'] == 'male') & (df['Age'] > 50)) | ((df['Sex'] == 'female') & (df['Age'] < 30))]
#     return result_df.to_json(orient='records')
#
#
# print(filter_passengers(pd.read_csv("..\\data\\titanic.csv")))
#

#Тест:

import pytest
import pandas as pd

# Здесь фикстура из теста предыдущего задания

# def test_filter_passengers(titanic_df):
#     expected_result = titanic_df.iloc[1:4].to_json(orient='records')
#     assert filter_passengers(titanic_df) == expected_result



'''Напишите функцию, которая вычислит среднюю стоимость билета на пассажира для каждого класса.
Функция принимает датафрейм и должна вернуть результат в виде словаря в формате JSON.'''


# import pandas as pd
# import json
#
# def fare_per_passenger_by_class(df):
#     total_fare_by_class = df.groupby('Pclass')['Fare'].sum()
#     total_passengers_by_class = df.groupby('Pclass')['PassengerId'].count()
#     avg_fare_per_passenger_by_class = total_fare_by_class / total_passengers_by_class
#     result_dict = avg_fare_per_passenger_by_class.to_dict()
#     return json.dumps(result_dict)
#
#
# print(fare_per_passenger_by_class(pd.read_csv("..\\data\\titanic.csv")))


# Тест:

import json
import pytest
import pandas as pd

# Здесь фикстура из теста предыдущего задания

# def test_fare_per_passenger_by_class(titanic_df):
#     expected_result = {'1': 62.2, '3': 7.3}
#     assert fare_per_passenger_by_class(titanic_df) == json.dumps(expected_result)



'''Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv. Функция должна отфильтровать 
пассажиров, у которых цена билета больше 50 и возраст меньше 30 лет. Затем функция должна отсортировать отфильтрованный 
DataFrame по имени пассажира в алфавитном порядке и вернуть результат.
Ожидаемый результат — отфильтрованный и отсортированный DataFrame.'''

# import pandas as pd
#
# def get_passengers(age: int, fare: float) -> pd.DataFrame:
#     '''фильтрация пассажиров'''
#     df = pd.read_csv('..\\data\\titanic.csv')
#     price_and_age_df = df.loc[(df.Age < age) & (df.Fare > fare)]
#     price_and_age_df.sort_values('Name', inplace=True)
#     return price_and_age_df
#
# result = get_passengers(30, 50.0)
# print(result.head())




'''Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv. Функция должна
сгруппировать пассажиров по классу и посчитать среднюю стоимость билета и количество пассажиров в каждом
классе. Функция должна вернуть результат в виде словаря в формате JSON.
Пример JSON-файла:

{
    "1st": {
        "average_ticket_price": 84.15,
        "passenger_count": 216
    },
    "2nd": {
        "average_ticket_price": 20.66,
        "passenger_count": 184
    },
    "3rd": {
        "average_ticket_price": 13.68,
        "passenger_count": 491
    }
}'''

# import pandas as pd
#
# def pass_agg(df: pd.DataFrame):
#     '''агрегация по классу и выборка цены и кол-ва пассажиров'''
#     grouped_df = df.groupby('Pclass').agg({'Fare': 'mean', 'PassengerId': 'count'})
#     dict_data = grouped_df.to_dict(orient='records')
#     result = dict()
#     for index, item in enumerate(dict_data):
#         result[f'{index + 1}st'] = {
#             'average_ticket_price': round(item['Fare'], 2),
#             'passenger_count': item['PassengerId']
#         }
#     return json.dumps(result, indent=4)
#
#
# df = pd.read_csv('..\\data\\titanic.csv')
# result = pass_agg(df)
# print(result)


'''Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv. Функция должна
отфильтровать пассажиров, которые выжили в катастрофе, и записать данные об этих пассажирах в файл
в формате JSON. Функция должна вернуть количество выживших пассажиров.
Пример JSON-файла:

[
    {
        "survived": 1,
        "pclass": 1,
        "name": "Allen, Miss. Elisabeth Walton",
        "sex": "female",
        "age": 29.0,
        "sibsp": 0,
        "parch": 0,
        "ticket": "24160",
        "fare": 211.3375,
        "cabin": "B5",
        "embarked": "S"
    },
    {
        "survived": 1,
        "pclass": 1,
        "name": "Allison, Master. Hudson Trevor",
        "sex": "male",
        "age": 0.92,
        "sibsp": 1,
        "parch": 2,
        "ticket": "113781",
        "fare": 151.55,
        "cabin": "C22 C26",
        "embarked": "S"
    },
    ...
]'''


import pandas as pd

def get_survived(df: pd.DataFrame) -> int:
    '''записать в файл json выживших и вернуть количество'''
    survived_df = df[df['Survived'] == 1]
    survived_df.to_json('survived.json', orient='records', indent=4, lines=True)
    return survived_df.count()


df = pd.read_csv('..\\data\\titanic.csv')
result = get_survived(df)
print(result)
