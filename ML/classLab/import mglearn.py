import mglearn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

# Загрузка данных
df = pd.read_csv("moons.csv")

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df['label'], test_size=0.25, random_state=0)

# Масштабирование данных
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# Создание и обучение модели MLPClassifier с активационной функцией tanh
mlp = MLPClassifier(activation='tanh', random_state=0)
mlp.fit(X_train, y_train)

# Визуализация разделяющей границы
mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.show()
