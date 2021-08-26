import re


texto1 = "Olá meu nome é Julia Fernandes"
texto2 = "Olá me chamo Marcelo Marcondes"
texto3 = "Olá meu nome é F3rnando Fernandes"

# compilar a expressão, já que ela será usada mais de 1 vez
regex = re.compile(r'([A-Z][a-z]+) ([A-Z][a-z]+)')

print(regex.findall(texto1))
print(regex.findall(texto2))
print(regex.search(texto3))
