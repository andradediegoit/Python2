# %% [markdown]
# # 1.Variáveis
# ## 1.1. Atribuição direta

# %%
x = 10 # Atribuição direta de um numero inteiro
y = 4.7 # Atribuição direta de um numero float
s = 'Python' # Atribuição direta de um caracter ou conjunto de caracteres
t = "Python" # Atribuição direta de um caracter ou conjunto de caracteres
r = '4' # Diferente de inteiro. 4 é uma string
w = '3' # Diferente de inteiro. 3 é uma string
v = "'3'" # Colocação de aplica em string
z = '"3"' # Colocação de aspas em string


# %%
r + w + s

# %% [markdown]
# ## 1.2. Atribuição por Construtor ou *Casting*

# %%
x1 = int(y) # Converter float para inteiro
x2 = float(x) # Converter inteiro para float

x3 = int(w) # Coverter sitring para inteiro. Operação válida se string contiver apenas numeros

# x4 = int(v) Operação inválida, uma vez que a string contem carateres

x5 = float(w) # Converter string para float
x6 = 27485487236782394874263784623784623
x7 = str(x6)

x8 = 'olá eu sou o "João".' + "O seu apelido é 'Araújo'"

print(x8)

# %%
x = 100


