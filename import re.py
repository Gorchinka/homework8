import re

input_string = input()

# Заменяем все идущие подряд пробелы на один
result = re.sub(' +', ' ', input_string)

print(result)
import re

input_string = input()

# Заменяем все идущие подряд пробелы и символы табуляции на один пробел
result = re.sub('[ \t]+', ' ', input_string)

print(result)