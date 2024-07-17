import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler #Для нормализации
from sklearn.utils import resample #Для выравнивания по классам

# Функция для удаления выбросов на основе правила "3 сигм"
def remove_outliers_3sigma(df, column):
    mean = df[column].mean()  # Вычисляем среднее значение
    std = df[column].std()  # Вычисляем стандартное отклонение
    lower_bound = mean - 3 * std  # Нижняя граница (3 сигмы)
    upper_bound = mean + 3 * std  # Верхняя граница (3 сигмы)
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]  # Фильтруем DataFrame по границам
    return df

# Функция для удаления неинформативных столбцов
def remove_infrequent_columns(df):
    threshold = 0.95
    columns_to_drop = []
    total_rows = len(df)
    for column in df.columns:
        value_counts = df[column].value_counts(normalize=True)
        most_common_count = value_counts.iloc[0]
        if most_common_count >= threshold:
            columns_to_drop.append(column)
    print(columns_to_drop)
    df.drop(columns=columns_to_drop, inplace=True)

# Путь к файлу CSV
input_file = 'C:/Users/lehak/Videos/ML/Lab2/dataset_invade.csv'

# Чтение CSV файла в DataFrame
df = pd.read_csv(input_file)
print(df)

# Определение качественных и количественных признаков
kol_features = [col for col in df.columns if df[col].dtype != 'object']
katch_features = [col for col in df.columns if df[col].dtype == 'object']

# Построение диаграммы плотности для качественных признаков 
for feature in katch_features: 
    df[feature].value_counts().plot(kind='bar') 
    plt.title(f'Диаграмма частот для {feature}') 
    plt.xlabel(feature) 
    plt.ylabel('Частота') 
    plt.show()

# Построение гистограмм для количественных признаков
for column in kol_features: 
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], color='skyblue', density=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Замена значений в столбце 'service' на их частоту встречаемости
service_value_counts = df['service'].value_counts(normalize=True)
df['service'] = df['service'].map(service_value_counts)#замена значений столбика сервайс на service_value_counts частота встречаемости

# Замена в столбике attack No and Yes на 0 и 1
df['attack'] = df['attack'].replace({"Yes": 1, "No": 0})

# Удаление неинформативных столбцов
remove_infrequent_columns(df)

# Определение качественных и признаков
katch_features = [col for col in df.columns if df[col].dtype == 'object']

# Преобразование качественных признаков в числовые
for column in katch_features: 
    dummies = pd.get_dummies(df[column], prefix=column, drop_first=False)#Преобразуем качественные признаки в набор бинарных значений, создавая столбик с префиксом
    df = pd.concat([df, dummies], axis=1)#Обьединяем бинарные признаки с исходным ДС
    df.drop(columns=[column], inplace=True)#исходные качественные признаки удаляются

# Замена значений True и False на 1 и 0
df = df.replace({True: 1, False: 0})

print(df)
# Определение количественных признаков
quantitative_features = [col for col in df.columns if col != 'attack' and df[col].dtype in ['int64', 'float64']]

# Нормализация/стандартизация всех количественных признаков
scaler = StandardScaler()#Создаем обьект класса
df[quantitative_features] = scaler.fit_transform(df[quantitative_features])#Обратившись к количественным значениям вычислим среднее значение и стандартное отклонение для каждого признака,
#затем стандартизирует признаки путем вычитания среднего значения и деления на стандартное отклонение. Это приводит к тому, что каждый признак будет иметь среднее значение 0 и стандартное отклонение 1. 

print(df)

# Удаление выбросов для всех количественных признаков
for feature in quantitative_features:
    if feature in df.columns:
        df = remove_outliers_3sigma(df, feature)  # Используем правило "3 сигмы"

# Удаление строк с пустыми значениями
df.dropna(inplace=True)

print(df)
# Выравнивание классов по объему
min_class_count = df['attack'].value_counts().min()  # Минимальное количество объектов в классе
balanced_df = pd.concat([resample(df[df['attack'] == 0], replace=True, n_samples=min_class_count), #находим кол-во классов 0 в признаке attack
                         resample(df[df['attack'] == 1], replace=True, n_samples=min_class_count)]) #находим кол-во классов 1 в признаке attack
balanced_df = balanced_df.sample(frac=1).reset_index(drop=True)  # Перемешиваем данные

# Вывод итогового датасета
print("\nИтоговый датасет после преобразований, нормализации, удаления выбросов и выравнивания классов:")
print(balanced_df)

# Путь для сохранения файла CSV
output_file = 'C:/Users/lehak/Videos/ML/Lab2/results.csv'
# Сохранение данных в файл CSV с отступом между столбцами
balanced_df.to_csv(output_file, index=False)
