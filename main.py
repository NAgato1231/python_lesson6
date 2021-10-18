s = "Техника такого уровня на меня не действует"
s3 = "Mokuton shinsu senju"
sub_i = "eх"
m4 = [1, 6, 5, 5, 'string', [3,2], 3.2]
susano = [2, 4, 6, 6, 'string', [7,1], 7.1]
naruto = ['Hashirama', 'Madara', 'Tobirama', 'Minato']
Madara = [2, 3, 5, 2, 11, 2, 7]
if __name__ == '__main__':
  m4.append("Teacher Genius")  # Добавляет элемент в конец списка
  m4.extend("TEACHER GENIUS")  # Расширяет список list, добавляя в конец все элементы списка L
  print(m4)
  o = ["Т", "Е" ,"Х", "Н", "И", "К", "А", "Б", "Е", "C", "К", "О", "Н", "Е", "Ч", "Н", "О", "Г", "О", "Ц", "У", "К",
  "У", "Ё", "М", "И"]
  m4.insert(1, o)  # Вставляет на i-ый элемент значение x
  print(m4)
  susano.remove(2)
  print(susano)  # Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
  removed_element = susano.pop(2)
  print('2', 2)  # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
  index = naruto.index('Madara')  # Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
  print(index)
  count = Madara.count(7)
  print('Count of 7:', count)  # Возвращает количество элементов со значением x
  Madara.sort()
  print(Madara)  # Сортирует список на основе функции
  Madara.reverse()
  print(Madara)  # Разворачивает список
  Madara.copy()
  print(Madara)  # Поверхностная копия списка
  Madara.clear()
  print(Madara)  # Очищает список





