# link da documentação : https://docs.python.org/3/library/string.html#formatexamples
print("Tentiva {1} de {0}".format(3, 10))
print("R$ {:f}".format(1.59))
print("R$ {:2f}".format(1.59))
print("R$ {:.2f}".format(1.59))
print("R$ {:.2f}".format(1234.5))
print("R$ {:7.2f}".format(1234.5))
print("R$ {:07.2f}".format(4.5))
print("R$ {:07d}".format(4))  # d = inteiro o 0 são os caracteres q serão preenchidos
print("R$ {:#7d}".format(4))  # d = inteiro o # são os caracteres q serão preenchidos
print("Data {:02d}/{:2d}".format(9, 4))  # d = inteiro o # são os caracteres q serão preenchidos
nome = 'Matheus'
print(f'Meu nome é {nome}')
print(f'Meu nome é {nome.lower()} com lower')
print(f'Meu nome é {nome.upper()} com upper')
nome = "matheus"
print(f'Meu nome é {nome.capitalize()} com capitalize')
nome = "  matheus  "
print(f'Meu nome é {nome} com strip')
print(f'Meu nome é {nome.strip()} com strip')
print("O nome possui a ? {}".format("a" in nome))

# nota_str = input("Digite sua nota")
# nota = float(nota_str)
# print("A nota digitada foi: ", nota)

NOME = input('Digite seu nome: ')
print(NOME.title())
