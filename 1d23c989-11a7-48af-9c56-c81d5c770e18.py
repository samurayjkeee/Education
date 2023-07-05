#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Александр, привет!👋</b>
# 
# Меня зовут Алексей Гриб, я буду твоим тимлидом на протяжении финального спринта:)
# 
# Сразу хочу предложить в дальнейшем общаться на "ты" - надеюсь, так будет комфортнее:) Но если это неудобно, обязательно дай знать, и мы придумаем что-нибудь ещё!
#     
# Цель ревью - не искать ошибки в твоём проекте, а помочь тебе сделать твою работу ещё лучше, устранив недочёты и приблизив её к реальным задачам аналитика. Поэтому не расстраивайся, если что-то не получилось с первого раза - это нормально, и это поможет тебе вырасти!
#     
# Ты можешь найти мои комментарии, обозначенные <font color='green'>зеленым</font>, <font color='gold'>желтым</font> и <font color='red'>красным</font> цветами, например:
# 
# <br/>
# 
# <div class="alert alert-success">
# <h2> Комментарий тимлида <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> похвала, рекомендации «со звёздочкой», полезные лайфхаки, которые сделают и без того красивое решение ещё более элегантным.
# </div>
# 
# <br/>
# 
# <div class="alert alert-warning">
#     <h2> Комментарий тимлида <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> некритичные ошибки или развивающие рекомендации на будущее. 
# </div>
# 
# 
# <br/>
# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Критичные ошибки, которые обязательно нужно исправить.
# </div>
# 
# Я не смогу принять проект, если в нём будет хотя бы одна критичная ошибка или несколько некритичных ошибок - тогда проект нужно будет немного доработать. Но это нестрашно - я обязательно дам тебе подсказку или укажу верное направление.
#     
# Пожалуйста, не удаляй мои комментарии, они будут особенно полезны для нашей работы в случае повторной проверки проекта. 
#     
# Ты также можешь задавать свои вопросы, реагировать на мои комментарии, делать пометки и пояснения - полная творческая свобода! Но маленькая просьба - пускай они будут отличаться от моих комментариев, это поможет избежать путаницы в нашем общении:)
# Например, вот так:
#     
# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# *твой текст*
# </div>
#     
# Давай посмотрим на твой проект!

# # Телеком — задача проекта
# 
# Оператор связи «Ниединогоразрыва.ком» хочет научиться прогнозировать отток клиентов. Если выяснится, что пользователь планирует уйти, ему будут предложены промокоды и специальные условия. Команда оператора собрала персональные данные о некоторых клиентах, информацию об их тарифах и договорах.
# 
# ### Описание услуг
# 
# Оператор предоставляет два основных типа услуг: 
# 
# 1. Стационарную телефонную связь. Возможно подключение телефонного аппарата к нескольким линиям одновременно.
# 2. Интернет. Подключение может быть двух типов: через телефонную линию (DSL*,* от англ. *digital subscriber line*, «цифровая абонентская линия») или оптоволоконный кабель (*Fiber optic*).  
# 
# Также доступны такие услуги:
# 
# - Интернет-безопасность: антивирус (*DeviceProtection*) и блокировка небезопасных сайтов (*OnlineSecurity*);
# - Выделенная линия технической поддержки (*TechSupport*);
# - Облачное хранилище файлов для резервного копирования данных (*OnlineBackup*);
# - Стриминговое телевидение (*StreamingTV*) и каталог фильмов (*StreamingMovies*).
# 
# За услуги клиенты могут платить каждый месяц или заключить договор на 1–2 года. Доступны различные способы расчёта и возможность получения электронного чека.
# 
# ### Описание данных
# 
# Данные состоят из файлов, полученных из разных источников:
# 
# - `contract_new.csv` — информация о договоре;
# - `personal_new.csv` — персональные данные клиента;
# - `internet_new.csv` — информация об интернет-услугах;
# - `phone_new.csv` — информация об услугах телефонии.
# 
# Во всех файлах столбец `customerID` содержит код клиента.
# 
# Информация о договорах актуальна на 1 февраля 2020.

# ### Данные :
# - customerID - код клиента;
# - gender - пол клиента;
# - SeniorCitizen - является ли клиент пенсионером;
# - Partner - наличие супруга(и);
# - Dependents - наличие иждивенцев;
# - BeginDate - дата начала договора;
# - EndDate - дата конца договора;
# - Type - тип договора;
# - PaperlessBilling - безбумажный биллинг;
# - PaymentMethod - способ оплаты;
# - MonthlyCharges - ежемесячные платежи;
# - TotalCharges - общие расходы;
# - InternetService - интернет подключение;
# - OnlineSecurity - блокировка небезопасных сайтов;
# - OnlineBackup - облачное хранилище файлов для резервного копирования данных;
# - DeviceProtection - антивирус;
# - TechSupport - выделенная линия технической поддержки;
# - StreamingTV - стриминговое телевидение;
# - StreamingMovies - каталог фильмов;
# - MultipleLines - несколько линий;

# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Хорошее вступление к проекту - здорово, что сделал его таким подробным, а также описал данные.

# ## Цель:
# - уменьшить отток клиентов, используя промокоды и специальные условия.
# ## Задачи:
# - загрузить датасет, посмотреть на данные, убрать пропуски, дубликаты
# - соединить все данные в одну таблицу и подготовить их для обучения моделей (кодирование и масштабирование признаков, оставить только нужные признаки, разобраться с целевым признаком)
# - разделить данные на обучающую и тестовую выборку
# - с помощью кросс-валидации подобрать параметры для нескольких моделей и добиться требуемых метрик
# - выявить лучшую модель и проверить на тестовой выборке
# - сделать вывод по проделанной работе
# 
# Вопросов нет.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> План получился хорошим и детальным, отлично - описаны все требуемые этапы работы над ML проектом.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Обрати только внимание, что кодирование важно делать __после__ сплитования выборок, а не перед.

# ## Подготовка данных

# In[1]:


import pandas as pd
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import lightgbm as lgb
import phik
from phik import resources, report
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from datetime import datetime
from sklearn.pipeline import Pipeline
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, make_scorer, confusion_matrix, plot_confusion_matrix,ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, make_pipeline


# Объеденение таблиц

# In[2]:


p1 = '/datasets/contract_new.csv'
p2 = '/datasets/internet_new.csv'
p3 = '/datasets/phone_new.csv'
p4 = '/datasets/personal_new.csv'

if os.path.exists(p1):
    contract = pd.read_csv(p1)
    internet = pd.read_csv(p2)
    phone = pd.read_csv(p3)
    personal = pd.read_csv(p4)
elif os.path.exists('contract_new.csv'):
    contract = pd.read_csv('contract_new.csv')
    internet = pd.read_csv('internet_new.csv')
    phone = pd.read_csv('phone_new.csv')
    personal = pd.read_csv('personal_new.csv')
else:
    print('Something is wrong')


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Библиотеки импортировали, данные загрузили - отлично!
# 
# При считывании данных из файла здорово перестраховывать себя от ошибок, связанных, например, с неверным указанием пути к файлу. А иногда бывает, что работаешь с файлом локально, выгружаешь его на сервер, ожидая, что он будет принимать данные, которые лежат на том же сервере, а код падает с ошибкой, потому что путь к файлу не поменялся с локального на серверный.
#     
# Для этого, например, можно использовать конструкцию `try-except`: сначала пробуешь локальный путь, при возникновении ошибки используется серверный путь (подробнее можешь почитать тут: https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html).
#     
# Но еще лучше использовать библиотеку `os` - её использование позволит тебе проверять существование указанных директорий (что может быть актуально при одновременной работа на локальном и сетевом окружении) и загружать данные из существующей директории, избегая ошибок. Как пример:
#     
#     import os
# 
#     pth1 = '/folder_1/data.csv'
#     pth2 = '/folder_2/data.csv'
#     
#     if os.path.exists(pth1):
#         query_1 = pd.read_csv(pth1)
#     elif os.path.exists(pth2):
#         query_1 = pd.read_csv(pth2)
#     else:
#         print('Something is wrong')
# 
# Ещё на этапе считывания данных можно спарсить дату: за это действие отвечает параметр `parse_dates` метода `read_csv()`, в него нужно передать список с названием полей-дат, и в большинстве случаев дата будет корректно преобразована в нужный формат сразу:)
# 
# Также на этапе считывания данных задать индекс-столбец- за это действие отвечает параметр `index_col`.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Это было рекомендацией, но окей:)

# In[3]:


df = personal.merge(contract,on='customerID',how='left')
df = df.merge(internet,on='customerID',how='left')
df = df.merge(phone,on='customerID',how='left')


# Посмотрим какие данные имеются, есть ли пропуски или дубликаты

# In[4]:


df


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Данные соединили корректно - никто не потерялся.

# In[5]:


df.info()


# In[6]:


df.isna().sum()


# In[7]:


df = df.fillna(value = 'No')


# Так как пропуски только в колонках, которые описывают доп.услуги, то пропуски в них имеет смысл принимать как отсутствие

# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Верно, хорошее решение для замены пропущенных значений.

# In[8]:


df.isna().sum()


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Пропуски удалили - отлично!

# In[9]:


df.duplicated().sum()


# Дубликатов нет 

# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Явные дубликаты отсутствуют - молодец, что проверяешь:)

# In[10]:


df


# In[11]:


df['TotalCharges'].sort_values()


# Видим что в колонке TotalCharges есть нулевые строчные значения

# In[12]:


df.loc[3331].TotalCharges


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть неявные пропуски - отлично!

# In[13]:


df.loc[df['TotalCharges']==' ','BeginDate'] 


# Видим что данные где TotalCharges пропущены только у тех пользователей, которые оформили подписку 2020-02-01, эти данные стоит убрать, так как не несут в себе важной информации.
# 

# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Верно, это новые пользователи.

# In[14]:


df.loc[df['TotalCharges']==' ','TotalCharges'] = df.loc[df['TotalCharges']==' ','MonthlyCharges']


# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Удалять этих пользователей не нужно: модель должна уметь работать в том числе с новоприбывшими клиентами. Тут стоит обработать неявыне пропуски и продолжать работать с этими клиентами.
#         
# Обязательно к учёту на этапе моделирования.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Для новых клиентов общие расходы приравнял к ежемесячным.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Окей.

# In[15]:


df['TotalCharges'] = df['TotalCharges'].astype(float)


# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Бездумо `copy()` тоже не стоит вставлять на любое предупреждение - всегда стоит читать содержимое. Тут проблема в способе приведения к типу данных - `loc` для этого использовать не нужно.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[16]:


df['TotalCharges'].sort_values()


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Преобразовали тип данных - отлично!

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Делая копию или срез какой-то таблицы (твой код - `df = df[df['BeginDate']!='2020-02-01']`), стоит использовать метод `copy()`: используя простое присвивание вида `a=b`, мы в переменную `a` помещаем не новый и самостоятельный объект в памяти, а всего лишь новую ссылку на объект в памяти, на который ссылается `b`. Как итог, внеся изменения в `a`, ты увидишь их и в `b`, и наоборот. Метод `copy()` позволяет создавать именно новые объекты в памяти.
#         
# Тогда не будет таких предупреждений.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Исправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[17]:


df.info()


# In[18]:


#df = df.replace(['No'],'0')
#df = df.replace(['Yes'],'1')


# Заменили значения Yes на 1 и No на 0 для дальнейшего обучения модели.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# 1. Кодирование переменных нужно выполнять после сплитования выборок - так мы можем контролировать появление в `test`/оперативных данных новые значения категориальных признаков, которые.
# 2. Нужно избегать ручного кодирования:
# - ручное кодирование нельзя встроить в `pipeline`, на которых строятся все промышленные решения;
# - при появлении новых значений категориальных признаков, не предусмотренных твоим решением, будут появляться ошибки или уязвимости в работе модели.
#         
# Поэтому кодирование нужно осуществлять после сплитования и с помощью энкодеров. Обязательно к учёту на этапе моделирования.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Убрал кодирование.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[19]:


df


# In[20]:


#ord_enc = OrdinalEncoder()
#df['PaymentMethod'] = ord_enc.fit_transform(df[['PaymentMethod']])
#df['Type'] = ord_enc.fit_transform(df[['Type']])|
#df['gender'] = ord_enc.fit_transform(df[['gender']])
#df['InternetService'] = ord_enc.fit_transform(df[['InternetService']])


# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Убрал кодирование.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[21]:


df


# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Аналогично - кодирование переменных нужно выполнять после сплитования выборок. Также обрати внимание, что `OrdinalEncoder()` подходит не ко всем моделям - учитывай это при выборе алгоритмов.
#         
# Обязательно к учёту на этапе моделирования.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[22]:


ax = df['TotalCharges'].hist(figsize=(15,6),bins=50);
ax.set_xlabel("TotalCharges");
ax.set_ylabel("кол-во");
ax.set_title('Общие расходы');


# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# На графиках нужно подписать оси Х и Y, а также названия.
#         
# Обязательно к учёту на этапе моделирования.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[23]:


ax = df['MonthlyCharges'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("MonthlyCharges");
ax.set_ylabel("кол-во");
ax.set_title('Ежемесячные расходы');


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть распределение непрерынвых признаков - отлично!

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# Добавил оси и названия.
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Важно также проанализировать распределение категориальных признаков. Кроме того, по результату анализа распределения должен быть вывод - по всем признакам.
#         
# Обязательно к учёту на этапе моделирования.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[24]:


ax = df['gender'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("gender");
ax.set_ylabel("кол-во");
ax.set_title('Пол клиента');


# In[25]:


ax = df['SeniorCitizen'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("SeniorCitizen");
ax.set_ylabel("кол-во");
ax.set_title('Пенсионный возраст');


# In[26]:


ax = df['Partner'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("Partner");
ax.set_ylabel("кол-во");
ax.set_title('Наличие супруга(и)');


# In[27]:


ax = df['Dependents'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("Dependents");
ax.set_ylabel("кол-во");
ax.set_title('Наличие иждивенцев');


# In[28]:


ax = df['Type'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("Type");
ax.set_ylabel("кол-во");
ax.set_title('Тип договора');


# In[29]:


ax = df['PaperlessBilling'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("PaperlessBilling");
ax.set_ylabel("кол-во");
ax.set_title('Безбумажный биллинг');


# In[30]:


ax = df['PaymentMethod'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("PaymentMethod");
ax.set_ylabel("кол-во");
ax.set_title('Способ оплаты');


# In[31]:


ax = df['InternetService'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("InternetService");
ax.set_ylabel("кол-во");
ax.set_title('Интернет подключение');


# In[32]:


ax = df['OnlineSecurity'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("OnlineSecurity");
ax.set_ylabel("кол-во");
ax.set_title('Блокировка небезопасных сайтов');


# In[33]:


ax = df['OnlineBackup'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("OnlineBackup");
ax.set_ylabel("кол-во");
ax.set_title('Облачное хранилище файлов для резервного копирования данных');


# In[34]:


ax = df['DeviceProtection'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("DeviceProtection");
ax.set_ylabel("кол-во");
ax.set_title('Антивирус');


# In[35]:


ax = df['TechSupport'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("TechSupport");
ax.set_ylabel("кол-во");
ax.set_title('Выделенная линия технической поддержки');


# In[36]:


ax = df['StreamingTV'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("StreamingTV");
ax.set_ylabel("кол-во");
ax.set_title('Стриминговое телевидение');


# In[37]:


ax = df['StreamingMovies'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("StreamingMovies");
ax.set_ylabel("кол-во");
ax.set_title('Каталог фильмов');


# In[38]:


ax = df['MultipleLines'].hist(figsize=(15,6),bins=30);
ax.set_xlabel("MultipleLines");
ax.set_ylabel("кол-во");
ax.set_title('Несколько линий');


# Вывод по данным: 
# 1. Нет явного избытка клиентов с определённым полом или с наличием супруга(супруги)
# 2. Пенсионеров в 6 раз меньше 
# 3. Клиентов без иждиевегцов также меньше в раза
# 4. Самый популярный тип договора помесячный 
# 5. Самый популярный способ оплаты электронный чек
# 6. Самый популярный тип подкючения fiber optic
# 7. Доп услуги в основном подключены у меншего кол-ва людей

# In[39]:


df['EndDate'].unique()


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Целевой признак сформирован корректно.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Единственное - с точки зрения нейминга мы не предсказываем `EndDate`, дата окончания контракта является инструментом формирования целевого признака, а не самим целевым признаком. Также при текущем подходе ты не сможешь оценить длительность контракта, так как полностью изменяешь признак, а длительность может быть очень важным признаком для нашей задачи. Поэтому стоит изменить поход к формирвоанию целевого признака.
#         
# Обязательно к учёту на этапе моделирования.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено, точечные замечания ниже.

# In[40]:


df.loc[df['EndDate']=='No','depart'] = 0
df.loc[df['EndDate']!='No','depart'] = 1


# In[41]:


df.loc[df['EndDate']=='No','EndDate'] = '2020-02-01'


# In[42]:


df['EndDate'] = pd.to_datetime(df['EndDate'],format='%Y-%m-%d')
df['BeginDate'] = pd.to_datetime(df['BeginDate'],format='%Y-%m-%d')
df['Duration'] = (df['EndDate'] - df['BeginDate']).dt.days


# In[43]:


df


# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Вся конструкция выглядит очень неоптимально:
# - использование циклов в `Pandas` - антипаттерн, от которого нужно уходить, так как итерирование по строкам может занимать очень много ресурсов;
# - хранить в одном столбце два вида объектов - `datetime` и `object` - неэффективно, нужно приводить к единообразному формату.
#     
# Здесь стоит начала выделить целевой признак, явно опираясь на значение `No`, далее заменить `No` на дату выгрузки, а уже потом весь столбец целиком приводить к `datetime` и считать признак длительности.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[44]:


ax = df.depart.hist(figsize = (15,6));
ax.set_xlabel('depart');
ax.set_ylabel('Кол-во')
ax.set_title('Ушедшие клиенты');


# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На графиках нето подписи осей Х и Y. Также важно прокомментировать дисбаланс.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[45]:


ax = df.loc[df['depart']==1,'gender'].hist();
ax.set_xlabel('gender');
ax.set_title('Пол ушедших клиентов');


# In[46]:


ax = df.loc[df['depart']==0,'gender'].hist();
ax.set_xlabel('gender');
ax.set_title('Пол оставшихся клиентов');


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Лишние столбцы удалили - отлично!

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Если удаляем `gender`, обязательно нужно обоснвоать это решение (не только на словах, но с помощью графиков или статистики).
#         
# Обязательно к учёту на этапе моделирования.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Добавил две колонки. Колонка duration показывает сколько времени клиент пользовался или пользуется услугами. Колонка depart показывает факт ухода клиента. По поводу пола, привидены графики, которые показывают, что факт ухода равновероятен у мужского и женского пола.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Отлично! Да, пол тут не особо влияет на что-то, можно сносить.
#     
# При анализе данных в задачах оттока интерес представляет распределение признаков в разрезе оттока - оставлю пару рекомендаций о том, как сделать его лучше:
# - при анализе непрерывных переменных интерес представляет диапазон значений, при которых отток выше, чем сохранение пользователей - для такого анализа можно использовать `sns.histplot()` с `hue` в качестве призака оттока, а также параметрами `stat='density'` и `common_norm=False`, также важно корректно настроить количество корзин для получения максимально наглядного результата - оно определяется по формуле `max() - min() + 1`, также можно настроить параметр `binwidth=1`;
# - при анализа категориальных/дискретных переменных нас также может интересовать, какое значение категории у признака более или менее отточное - для этого можно построить `sns.barplot()` с `x` в качестве признака, `y` в качестве признака оттока, а также `plt.axhline()` со средним уровнем оттока по компании для формирования трешхолда, при сравнении с котором мы бы определили, выше отток или ниже, чем в компании в среднем.

# In[47]:


df = df.drop(columns = ['customerID','BeginDate','EndDate','gender'])


# In[48]:


df


# In[49]:


df.info()


# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Типы данных изменили - окей, порядок.

# Вывод по подготовке данных : 
# 
# 1. загружены 4 датасета и объеденены в один
# 2. дубликатов не обнаружено
# 3. убраны неинформативные клиенты
# 4. значения NaN заменены на отсутсвие услуг
# 5. выбросов и аномальных значений в колонка TotalCharges и MonthlyCharges не найдено
# 6. категоральные данные закодированы
# 7. данные приведены к численному типу
# 

# <div class="alert alert-success">
# <h2> Комментарий тимлида (план) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Небольшой промежуточный вывод - отлично!

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Комментарий тимлида: общий вывод по проекту (план) </b>
# 
# Александр, хороший старт работы над проектом - план получился довольно подробным и обстоятельным, также сделан хороший старт для полноценного EDA данных проекта.
#     
# Обрати внимание на комментарии жёлтого цвета - не делаю их красными, чтобы ты приступил к следующему этапу проекта, но на этапе моделирования нужно будет учесть комментарии, где об этом явно указано.
#     
# План принят, жду тебя на следующем этапе работы над проектом:)

# ## Моделирование

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На вводной встрече я говорил о том, что техники балансирования классов важно использовать в составе `pipeline`: применяя `upsampling` до сплитования, ты создаёшь дубликаты наблюдений положительного класса, которые после сплитования распределяютяя по `train` и `test`, в результате одни и те же наблюдения участвуют в обучении и тестировании, что создаёт нам утечку и делает метрику оптимистично высокой.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Решил не использовать upsampling, т.к. получил удовлетворяющие метрики без него.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[50]:


features = df.drop(columns = 'depart')
target = df['depart']


# In[51]:


features_train, features_test, target_train, target_test = train_test_split(features,target,test_size = 0.25, 
                                                                            random_state = 220523,stratify=target)


# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Сплитование выполнено корректно: пропорции соблюдены, контсанта соответствует значению группы. Также можно было бы выполнить стратификацию целевого признака, чтобы в выборках был равный баланс классов (без `upsampling`).

# In[52]:


category = ['SeniorCitizen','Partner', 'Dependents', 'Type', 'PaperlessBilling',
       'PaymentMethod', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'MultipleLines']
numeric = ['MonthlyCharges','TotalCharges','Duration']


# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Выделили категориальные признаки.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Признак `SeniorCitizen` хоть и представлен как численная величина, по своей природе является дискретным, поэтому аналищироваться должен как категориальный признак.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[53]:


ord_enc = OrdinalEncoder()
features_train[category] = ord_enc.fit_transform(features_train[category])
features_test[category] = ord_enc.transform(features_test[category])


# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Закодировали категориальные переменные порядковым кодированием - отлично!

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# У `OrdinalEncoder()` тоже стоит настраивать бесперебойную работу, чтобы не останавливать процесс работы модели при появлении новых значений категориальных признаков - для этого можно настроить `handle_unknown='use_encoded_value'`, чтобы неизвестные значения заменялись константным значением, а само константное значение настраивается в параметре `unknown_value` - туда стоит пердать очень редкое значение константы, маловероятное на практике.

# In[54]:


scaler = StandardScaler()
features_train[numeric] = scaler.fit_transform(features_train[numeric])
features_test[numeric] = scaler.transform(features_test[numeric])


# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Выполнили масштабирование непрерывных признаков - отлично!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# 1. Инструменты трансформации выборок нельзя обучать на `test`: так как `test` выборка имитирует поток реальных данных, с которыми работает модель, то, во-первых, `test` выборки в реальной среде работы модели не будет, и твой пайплайн с моделью упадёт, во-вторых, так мы даём модели данные из будущего, которые в нормальных условиях она не могла бы увидеть - в `test` вполне могут быть новые категории, отсутствующие в `train` (если говорить про кодирование), или распределение переменных в `test` может сильно отличаться от распределения в `train` (если говорить про стандартизацию).
#     
#     Единственно верный порядок работы с такими инструментами - обучаемся на `train` (для `train` можно использовать `fit_transform()`), и уже обученным на `train` инструментом изменяем выборки `train`, `test` и `valid` (если выделялась).
#     
# 2. Ты масштабируешь не только непрерывные, но и закодированные категориальные переменные - таким образом они теряют своё исходное содержание и становятся бессмысленными. Масштабировать нужно только непрерывные признаки.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# Данные закодированы и отмасштабированы.

# In[55]:


fig, ax = plt.subplots(figsize=(16,10)) ;
sns.heatmap(df.phik_matrix(interval_cols=['MonthlyCharges', 'TotalCharges', 'Duration']),annot=True, cmap='coolwarm', center=0,ax=ax);


# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть анализ матрицы корреляций - отлично! Круто, что используешь `phik` для анализа корреляции между признаками разного типа.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Матрицу корреляций удобнее воспринимать в виде тепловой карты - например, `sns.heatmap()`, также можно использовать параметры `annot=True, cmap='coolwarm', center=0` для повышения информативности тепловой карты.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Не настроен параметр `interval_cols` при работе с матрицей корреляций `phik` - на вводной встрече я акцентировал внимание на важности этого момента, так как если не задавать список непрерывных признаков явно, библиотека будет делать это сама, и зачастую делает это неправильно, в результате получаем смещённые оценки корреляции.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[56]:


results = pd.DataFrame({
    'model':[],
    'roc_auc':[],
    'accuracy':[],
    'best_param':[]
})
scoring = {'AUC':'roc_auc','Accuracy':'accuracy'}
def train_model(model, parameters):
    
    model_random = GridSearchCV(
        model,
        parameters,
        scoring=scoring,
        refit='AUC'
    )
    
    model_random.fit(features_train,target_train)
    # высчитаем метрики
    roc_auc = pd.DataFrame(model_random.cv_results_).sort_values('mean_test_AUC')['mean_test_AUC'].iloc[-1]
    accuracy = pd.DataFrame(model_random.cv_results_).sort_values('mean_test_AUC')['mean_test_Accuracy'].iloc[-1]
    print('Best parameters:', model_random.best_params_)
    print('roc_auc:', roc_auc)
    print('accuracy:', accuracy)
    
    results.loc[ len(results.index )] = [model_random.best_estimator_,roc_auc,accuracy,model_random.best_params_]


# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Неплохой инструмент для поиска лучшей модели.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Для `Accuracy` необязательно делать `make_scorer`, так как эта метрика тоже имеет строковый алиас по аналогии с `AUC-ROC`.

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Если делаешь оптимизацию по двум метрикам, то и в выводе нужно выводить две метрики, иначе в двумя метриками работать нет смысла.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Не совсем понял как выводить сразу две метрики, поэтому оставил выводить только roc-auc.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено. Две метрики нужно выводить из `cv_results_` с сортировкой по основной метрике.

# In[57]:


lgbm_param = {'learning_rate': [ 0.01, 0.05, 0.1],
          'n_estimators': [50, 100, 150],
          }

lgbm = lgb.LGBMClassifier(random_state=220523,                    
    boosting_type='gbdt',
    n_jobs=-1
)

train_model(lgbm, lgbm_param)


# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Для `LGBMClassifier` оптимизировали гиперпараметры и оценили модель на кросс-валидации.
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b>  Ранее уже был выполнен баланс классов, поэтому нет смысла в балансировании классов с помощью `class_weight`. Без балансирования тоже нет смысла, потому что `AUC-ROC` нечувствителен к дисбалансу.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[58]:


cat_param = {'max_depth': range(1, 7),
          'learning_rate': [0.01, 0.1],
          'n_estimators': [50, 100, 150]
          }

cat = CatBoostClassifier(verbose=False, random_state=220523)

train_model(cat, cat_param)


# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Для `CatBoostClassifier` оптимизировали гиперпараметры и оценили модель на кросс-валидации.
# </div>

# In[59]:


rand_for_param = {
    "n_estimators" : [50, 100, 150],
     "max_depth" : range(1, 6)
}

rand_for = RandomForestClassifier(class_weight='balanced',random_state=220523)

train_model(rand_for,rand_for_param)


# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Для `RandomForestClassifier` оптимизировали гиперпараметры и оценили модель на кросс-валидации.
# </div>

# In[60]:


display(results)


# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Хорошая сравнительная характеристика моделей.

# Лучшей показала себя модель CatBoostClassifier(learning_rate = 0.1, max_depth = 4, n_estimators = 250), на обучающей выборке она показала лучший результат auc-roc = 0.889.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Нужно сделать вывод о лучшей модели.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Поправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[61]:


cat = lgb.LGBMClassifier(n_estimators=300, learning_rate = 0.1, random_state=220523)
cat.fit(features_train,target_train)
pr = cat.predict(features_test)
print('AUC_ROC:',roc_auc_score(target_test,cat.predict_proba(features_test)[:, 1]))
print('Accuracy:',accuracy_score(pr,target_test))
cm = confusion_matrix(pr,target_test)


# In[62]:


cmp = ConfusionMatrixDisplay(confusion_matrix=cm);
cmp.plot();


# Матрица ошибок показывает, что модель очень хорошо предсказывает истинно отрицательные результаты (вероятность предсказать правильно 0,91 ), в случае истинно положительных вариантов, модель работает не так хорошо (вероятность предсказать правильно 0,81).

# In[63]:


pd.Series(cat.feature_importances_, index=features_train.columns).sort_values(ascending=False)


# Наиболее значимые признаки - Duration, MonthlyCharges, TotalCharges. Признаки StreamingTV и InternetService практически не вносят вклад в модель.

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть оценка модели на `test` - отлично!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Для оценки `AUC-ROC` нужно использовать не метки классов, а вероятности отнесения к положительному классу.
#     
# Также нужно исследовать важность признаков лучшей модели.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Не совсем понял по поводу auc-roc.
# </div>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> В `roc_auc_score` нужно передавать `target` и вероятности отнесения метки к целевому классу, ты передаёшь сами классы. Используй метод `.predict_proba()` и выбери нужный столбец массива для работы.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Исправил.
# </div>

# <div class="alert alert-success">
# <h2> Комментарий тимлида (код) v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b>  При решении задач классификации, особенно с дисбалансом классов, нужно строить и анализировать матрицу ошибок, чтобы помочь бизнесу оценить условно-реальный эффект от работы модели и принять объективное решение о работе с ней.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Добавил матрицу ошибок.
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> Её нужно также интерпретировать.

# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# Исправил.
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) v.3 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> `в случае истинно положительных вариантов, модель работает не так хорошо (130 из 149, т.е. вероятность предсказать правильно 0,81).` - кажется, цифры не соответствуют содержимому матрицы - к исправлению на этапе отчёта.

# Общий вывод:
# 1. Данные разбиты на обучающие и тестовые выборки.
# 2. Использвалось кодирование и масштабирование (OrdinalEncoding, StandartScaler).
# 3. Построенна тепловая карта по матрице корреляций, по ней можно сказать, что ключевыми признаками, которые влияют на целевой признак, являются TotalCharges и Duration.
# 4. Обучено 3 модели (RF,Cat,LGBM).
# 5. Лучшие метрики  показал LGBMClassifier(n_estimators=300, learning_rate = 0.1, random_state=220523), на обучающей выборке она показала лучший результат roc_auc: 0.8746791949133479, accuracy: 0.892274268226255, а на тестовой выборке показал AUC_ROC: 0.8976936253517681, Accuracy: 0.9085746734809768
# 6. По модели можно сказать, что она лучше справляется с истинно отрицательными вариантами.

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть небольшой вывод - отлично!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Вывод по проекту нужно будет актуализировать с учётом замечаний.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Актуально.

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> Его также неплохо было бы обогатить результатами других исследований, а то он вышел очень уж скромный.

# <div class="alert alert-warning">
#     <h2> Комментарий тимлида (код) v.2 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> Актуально.

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (код) v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Комментарий тимлида: общий вывод по проекту (код) </b>
# 
# Алексадр, хороший старт работы над проектом - сделана крепкая основа будущего крутого проекта:)
#     
# В любой работе есть точки роста - основные отмечены комментариями красного цвета и являются обязательными к использованию. Менее значительные отмечены зелёными (где сделано хорошо, но можно сдедать лучше) и жёлтыми (где сделано не очень оптимально и что стоило бы улучшить уже сейчас) комментариями - их учёт опционален, но повысит общее качество работы.
#     
# Жду тебя на следующей итерации:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Комментарий тимлида: общий вывод по проекту (код) v.2 </b>
# 
# Алексадр, продолжаем работу над проектом - актуальные замечания отмечены комментариями с меткой `v.2`.
#     
# Жду тебя снова:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Комментарий тимлида: общий вывод по проекту (код) v.3 </b>
# 
# Алексадр, с этапом кода закончили - жду твой отчёт по проекту:)

# ## Отчёт

# 1. Было загружено 4 датасета и объеденины в один.
# 2. В датасеты обработались пропуски и дубликаты.
# 3. Рассмотрены распределения признаков .
# 4. Выделен целевой признак(depart) и сформирован новый признак(duration) на основе других.
# 5. Данные приведены к соответсвующим типам.
# 6. Удалены неинформативные и ненужные в дальнейшем исследовании колонки.
# 7. Данные подготовлены к ML (сплит, кодировка, масштабирование)
# 8. Рассмотерна матрица корреляций
# 9. Обучено 3 модели и выбрана лучшая (LGBM)
# 10. Лучшая модель проверена на тестовой выборке и показала удовлетворительные результаты
# 11. Рассмотерна матрица ошибок
# 12. Сделаные выводы по модели
# 
# Проведённая работа соответсвует ранее запланированому плану.

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (отчёт) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Выделены ключевые шаги работы над проектом. Работа была по плану.

# Основная сложность заключалась в подготовке данных для ML. В датасете присутствовали клиенты которые на момент выгрузки не имели значений в общих расходах, для таких клиентов общий расход приравнивался к ежемесячному. Целевой признак, который фиксировал факт ухода клиента, был сформирован на основе колонки EndDate. Так же добавился новый признак, который учитывал длительность пользования услугами клиента.

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (отчёт) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Описаны сложности и пути решения.

# Итоговый список признаков: 
# - SeniorCitizen - является ли клиент пенсионером;
# - Partner - наличие супруга(и);
# - Dependents - наличие иждивенцев;
# - Type - тип договора;
# - PaperlessBilling - безбумажный биллинг;
# - PaymentMethod - способ оплаты;
# - MonthlyCharges - ежемесячные платежи;
# - TotalCharges - общие расходы;
# - InternetService - интернет подключение;
# - OnlineSecurity - блокировка небезопасных сайтов;
# - OnlineBackup - облачное хранилище файлов для резервного копирования данных;
# - DeviceProtection - антивирус;
# - TechSupport - выделенная линия технической поддержки;
# - StreamingTV - стриминговое телевидение;
# - StreamingMovies - каталог фильмов;
# - MultipleLines - несколько линий;
# - depart - факт ухода клиента;
# - Duration - длительность пользованием услугами
# 
# Категоральные признаки 
# 
#     category = ['SeniorCitizen','Partner', 'Dependents', 'Type', 'PaperlessBilling',
#        'PaymentMethod', 'InternetService',
#        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
#        'StreamingTV', 'StreamingMovies', 'MultipleLines']
#        
# Кодировались с помощью OrdinalEncoder(), а количественные признаки 
#     
#     numeric = ['MonthlyCharges','TotalCharges','Duration']
#     
# масштабировались с помощью StandardScaler().

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (отчёт) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Описан интовый набор данных и их подготовка для моделирования.

# ### Сводная таблица исследованных моделей и их метрика на кросс-валидации.

# In[64]:


display(results)


# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (отчёт) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть сравнение промежуточных результатов модели.

# ### Лучшая модель : 
# LGBMClassifier()
# 
# Обучение:
# - Best parameters: {'learning_rate': 0.1, 'n_estimators': 150}
# - roc_auc: 0.8709661819067562
# - accuracy: 0.8862156331527192
# 
# Тест:
# - AUC_ROC: 0.8976936253517681
# - Accuracy: 0.9085746734809768
# 

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (отчёт) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Описана лучшая модель и её результаты на `test`.

# ### Важность признаков

# In[65]:


pd.Series(cat.feature_importances_, index=features_train.columns).sort_values(ascending=False)


# Наиболее значимые признаки - Duration, MonthlyCharges, TotalCharges. Признаки StreamingTV и InternetService практически не вносят вклад в модель.

# <div class="alert alert-success">
#     
# <h2> Комментарий тимлида (отчёт) <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Оценили важность признаков - отлично!

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Комментарий тимлида: общий вывод по проекту (отчёт) </b>
# 
# Александр, отчёт принят - поздравляю с завершением финального спринта!
#     
# Проделана без сомнения классная работа: тебе удалось сделать проект высокого качества и решить довольно популярную боевую задачу классификации с дисбалансом классов на достаточно хорошем уровне - думаю, ты теперь без труда сможешь решать такие задачи в практической деятельности.
#     
# Из положительных моментов могу отметить следующее:
# - чистый и понятный код, соответствие PEP8, последовательность и структурность работы - есть ощущение цельного и законченного исследования, несущего ценность для заказчика, что и является нашей конечной целью;
# - попробованы разные модели, оптимизированы гиперпараметры, есть оценка на кросс-валидации - работа, которая не оставляет места для плохой метрики, очень основательный подход к решению задачи;
# - для оптимизации гиперпараметров использован `GridSearchCV` - хороший выбор, так как многие выбирают по старинке - циклом и кросс-валидация. Здорово, что используешь автоматизированные инструменты, которые выполняют рабтоту эффективно.
# 
# Есть несколько рекомендаций об инструментах, которые не были использованы в проекте и которые хотел бы отметить:
# - визуализация: `matplotlib` покрывает базовую потребность в визуализации информации, однако рекомендую изучить библиотеку `plotly`: она рисует красивые и интерактивные графики, которые очень любит бизнес, и ценность твоих отчётов будет выше, если качество визуализации выйдет на новый уровень;
# - оптимизация гиперпараметров: `GridSearchCV` и аналоги всё ещё в ходу и пока не сдают позиции, но сейчас довольно популярны алгоритмы оптимизации вроде `Optuna` или `Hyperopt` - более интеллектуальные, чем простой перебор, и работают быстрее иной раз. Рекомендую разобраться в них и начать применять в практической деятельности;
# - `pipeline`: практически все решения сейчас делаются в конвейерах, это удобно с точки зрения масштабирования, деплоя и обслуживания. Очень рекомендую разобраться с этим инструментом - это очень упростит работу в будущих проектах;
# - `make_column_transformer`: ты отлично пользуешься энкодерами, правильно подбирая и настраивая их в зависимости от данных и используемых моделей. Следующим этапом можно научиться пользоваться трансформером, который соединяет в себе несколько энкодеров в единый инструмент - `make_column_transformer` (https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html). Его можно удобно настраивать для преобразования отдельных признаков отдельными инструментами, также он легко встраивается в `pipeline` и может стать сильным этапом твоего конвейрера;
# - матрица ошибок: этим инструментом стоит научиться пользоваться и применять в работе, так как он позволяет бизнесу оценивать потенциальный эффект от внедрения модели в работу. `True Positive` и `True Negative` - это полезные метрики для бизнеса, определяющие ценность модели для их процессов, но `False Positive` и `False Negative` - это уязвимые места твоей модели и риски для процессов, так как они могут формировать убытки для компании, нерентабельные затраты и другие негативные факторы. Поэтому уделять внимание стоит не только правильным ответам, но и ошибкам, чтобы получить компексную оценку модели, в том числе её слабых мест;
# - отбор признаков: хорошо анализировать важность признаков, но чем меньше признаков будет в итоговом наборе, тем быстрее модель будет учиться, также это может привести к росту метрики (не всегда, но бывает периодически 😁). Для отбора признаков можно использовать корреляцию, результаты исследования важности признаков итоговой модели и последующую новую итерацию обучения-тестирования, а также инструменты отбора признаков `feature_selection` у `sklearn`: https://scikit-learn.org/stable/modules/feature_selection.html. Их, кстати, можно делать частью `pipeline` - твои конвейеры будут ещё лучше.
#     
# Если планируешь размещать работу в портфолио - ты можешь учесть рекомендации выше в работе самостоятельно, удалить наши комментарии и сделать очень презентабельное решение для демонстрации полученных навыков. Лучше это сделать в ближайшее время, пока все нюансы еще отложились в памяти.
#     
# Также дам пару рекомендаций в целом о дальнейшей карьере:
# - табличные данные и классический ML - это интересно, но постепенно отходит на второй план по мере роста популярности нейронных сетей и глубокого обучения. Поэтому рекомендую активно в них погружаться, выбрать близкую душе специализацию (CV или NLP) и осваивать её;
# - Python - must have: важно не только хорошо уметь работать с алгоримами машинного обучения, но и деплоить решения, настраивать пайплайны и миграции, писать качественный, чистый и отказоустойчивый код, чтобы быть хорошим ML инженером - это тоже очень важный аспект деятельности дата сайентиста, поэтому тут тоже очень больше поле для деятельности;
# - облачные технологии: сейчас всё меньше заказчиков работают на собственных мощностях, отдавая предпочтения облачной инфраструктуре: она проще в обслуживании и масштабировании и позволяет экономить на железе. Сейчас многие технологические гиганты типа AWS, MS и др. имеют собственные облачные решения, которые они продают как продукты - хорошее понимание облачных технологий будет твоим сильным конкурентным преимуществом. На сайтах этих компаний много обучающих курсов, рекомендую уделить этому внимание.
#     
# После окончания финального спринта у нас будет заключительная консультация, где мы сможем подвести итоги и обсудить несколько проектов. Есть возможность выступить перед сокурсиниками со своим проектам в Zoom - напиши мне об этом в Пачку, если есть желание :)
#     
# Спасибо за отличную работу над проектом, желаю продуктивного дальнейшего развития и лёгкого трудоустройства, если актуально:) Надеюсь увидеть тебя на заключительной консультации:) 
