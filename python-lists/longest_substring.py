# Реализуйте функцию find_longest_length(), принимающую на вход строку 
# и возвращающую длину максимальной последовательности 
# из неповторяющихся символов. 
# Подстрока может состоять из одного символа. Например в строке qweqrty
# можно выделить следующие подстроки: qwe, weqrty. 
# Самой длинной будет weqrty, а её длина — 6 символов.


def find_longest_length(string):
  """Принимает строку и возвращает
  число уникальных символов
  """
  length = len(string) + 1
  for i in string:
    if string.count(i) > 1:
      length -= 1
  return length
