
from itertools import permutations

lista = ['Adelaide Soares','Adriana Diniz', 'Amenaide Brito','Ana Nogueira','Angélica Pires','Bruna Mariane','Cida Lança','Cida Pereira','Cida Silva','Cida Souza','Cristiane Santos','Deolinda Campos','Diana','Elaine Assis','Elena Borges','Erlaine Nogueira',
'Eunice Fiori','Josefa','Laisa Souza','Livia Diniz','Maria Alves','Marlene Patel','Nilza','Roseli','Sandra Minharo','Sheila Farias']

for combinacao in permutations(lista, 2):
    print(combinacao)

