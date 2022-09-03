#тестовое задание
import pandas as pd

from yargy import Parser, rule, or_, and_, not_
from yargy.predicates import gram, dictionary

data = pd.read_csv('test_data.csv')

Manager = data[(data['role'] == 'manager')].drop(columns = ['line_n','role'], axis = 1)

text = ''
for n in range(0,6):
  for i in range(Manager['dlg_id'].value_counts()[n]):
    text += Manager[(Manager['dlg_id'] == n)]['text'].iloc[i] + '.'
  text+='\n' #искусственное добавление разделителя
text = text.strip('\n').split('\n') #удаление конечного лишнего разделителя и преобразование строки в список строк
text = [x.lower() for x in text]

Name = rule(
    or_(dictionary({'зовут', 'имя'}), gram('Name')), or_(gram('Name'),dictionary({'зовут', 'имя'}))
)

COMPANY =or_(
    rule (dictionary({'компания', 'организация'}),gram('nomn'),gram('nomn')),
    rule (dictionary({'компания', 'организация'}),gram('nomn'))
)

test1 = [Name, COMPANY]

for i in range(0,6):
  print(f'Диалог номер {i+1}:')
  for m in range(len(test1)):

    parser = Parser(test1[m])
    for match in parser.findall(text[i]):
      bool = match.span< [100,100]
      if bool == True:
        print([x.value for x in match.tokens])

      else:
        pass

hello = ["здравствуйте", "привет", "добрый день", "добрый вечер", "доброе утро", "добро пожаловать"]
bye = ["пока", "до свидания", "до скорого", "увидимся", "хорошего дня", "хорошего вечера", "счастливо",
       "счастливого пути", "всего доброго"]

test_hello = []
test_bye = []
for i in range(0, 6):
    text_hi = text[i].split('.')[0]
    text_bye = text[i].strip('.').split('.')[-1]

    for m in range(len(hello)):
        if hello[m] in text_hi:
            print(f'Приветствие, диалог {i + 1}:', hello[m])
            test_hello.append(1)

    for m in range(len(bye)):
        if bye[m] in text_bye:
            print(f"Прощание, диалог {i + 1}:", bye[m])
            test_bye.append(1)

if len(test_hello)<6 or len(test_bye)<6:
    print('Менеджер не выполняет требование: в каждом диалоге поздороваться и попрощаться с клиентом')
else:
    print('Менеджер выполняет требование: в каждом диалоге поздороваться и попрощаться с клиентом')