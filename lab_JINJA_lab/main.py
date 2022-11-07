from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

f_template = open('ind_test_template.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('macros.html')

student =[
 ["Алина", "Бизнес-информатика", ["Базы данных",
 "Программирование", "Эконометрика", "Статистика"], "ж"],
 ["Вадим", "Экономика", ["Информатика", "Теория игр",
 "Экономика", "Эконометрика", "Статистика"], "м"],
 ["Ксения", "Экономика", ["Информатика", "Теория игр",
 "Статистика"], "ж"]
 ]

def add_spaces(text):
 return " ".join(text)

def dis_count(dis):
 if (dis == 1):
  return "1 дисциплину"
 elif (dis == 2):
  return "2 дисциплины"
 elif (dis == 3):
  return "3 дисциплины"
 elif (dis == 4):
  return "4 дисциплины"
 elif (dis == 5):
  return "5 дисциплин"

template.globals["add_spaces"] = add_spaces
template.globals["len"] = len
template.globals["dis_count"] = dis_count
result_html = template.render(user = student[1])


#создадим файл для HTML-страницы
f = open('test.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()




