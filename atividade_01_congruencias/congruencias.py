# Atividade 1 - Parte A: verificação de congruência modular
#
# Objetivo: verificar se a e b são congruentes módulo n.
# Isso acontece quando a diferença (a - b) é divisível por n.
# Exemplo: 23 - 8 = 15. Como 15 é múltiplo de 5,
# podemos dizer que 23 e 8 são congruentes módulo 5.

# print() mostra uma mensagem na tela.
print("CONGRUÊNCIA MODULAR")

# input() lê o que o usuário digita e devolve um texto.
# int() converte esse texto em um número inteiro para fazer os cálculos.
# a e b podem ser positivos, negativos ou zero.
a = int(input("Digite o inteiro a: "))
b = int(input("Digite o inteiro b: "))

# n é o módulo: será o divisor usado para calcular o resto.
# O enunciado exige que n seja maior que zero.
n = int(input("Digite o módulo n (maior que zero): "))

# while significa "enquanto". O sinal <= significa "menor ou igual".
# Enquanto n for zero ou negativo, o programa pede outro valor.
# Usamos while porque o usuário pode digitar um valor inválido várias vezes.
while n <= 0:
    print("O módulo deve ser maior que zero.")
    n = int(input("Digite novamente o módulo n: "))

# Esta linha já está fora do while: só chegamos aqui quando n é positivo.
# Primeiro, calculamos a diferença que queremos testar.
diferenca = a - b

# Em Python, % calcula o RESTO da divisão.
# Exemplo: 15 % 5 resulta em 0, porque 15 = 5 × 3 + 0.
# Já 14 % 5 resulta em 4, porque 14 = 5 × 2 + 4.
resto = diferenca % n

# Mostramos a diferença e o resto para justificar a resposta.
# O f antes das aspas permite inserir os valores das variáveis entre { }.
# O \n pula uma linha para separar o cálculo da entrada de dados.
# Os parênteses em torno de b ajudam na leitura se b for negativo: 7 - (-3).
print(f"\nDiferença: {a} - ({b}) = {diferenca}")
print(f"Resto da divisão de {diferenca} por {n}: {resto}")

# if significa "se". Aqui, == compara dois valores.
# Atenção à diferença: "resto = ..." guarda um valor na variável;
# "resto == 0" pergunta se o valor guardado é igual a zero.
if resto == 0:
    # Resto zero: n divide a diferença exatamente.
    # Pela definição matemática, a e b são congruentes módulo n.
    print(f"Como o resto é zero, {a} e {b} são congruentes módulo {n}.")
else:
    # else significa "senão". Este bloco só executa se o resto não for zero.
    # Nesse caso, a diferença não é múltipla de n.
    print(f"Como o resto não é zero, {a} e {b} não são congruentes módulo {n}.")

# Atividade 1 - Parte B: Teorema Chinês do Resto
# Etapa 1: ler as congruências que formam o sistema.

print("\nTEOREMA CHINÊS DO RESTO")

# O usuário escolhe quantas congruências o sistema terá.
# O enunciado permite apenas duas opções: 3 ou 4.
quantidade = int(input("Quantas congruências deseja informar (3 ou 4)? "))

# "not in" significa "não está entre".
# Enquanto a escolha não for 3 nem 4, pedimos outro valor.
while quantidade not in (3, 4):
    quantidade = int(input("Escolha 3 ou 4: "))

# Criamos uma lista vazia para guardar as congruências.
# Cada item será um par (resto, módulo).
# Exemplo: o par (2, 3) representa x ≡ 2 (mod 3).
congruencias = []

# O for repete a leitura uma vez para cada congruência.
# Em range(), o limite final não é incluído. Por isso usamos quantidade + 1:
# se quantidade for 3, o índice assumirá os valores 1, 2 e 3.
for indice in range(1, quantidade + 1):
    print(f"\nCongruência {indice}:")

    # Aqui o resto é INFORMADO pelo usuário. Na Parte A, ele era calculado.
    resto_informado = int(input("Digite o resto: "))
    modulo = int(input("Digite o módulo: "))

    # Todos os módulos do sistema precisam ser positivos.
    # Se este módulo for inválido, corrigimos apenas ele.
    while modulo <= 0:
        print("Esse módulo está fora das condições da atividade.")
        modulo = int(input("Digite um módulo maior que zero: "))

    # Os parênteses internos formam o par (resto, módulo).
    # append() acrescenta esse par à lista sem apagar os anteriores.
    congruencias.append((resto_informado, modulo))

# Este print está fora do for: aparece depois que o sistema inteiro foi lido.
print("\nSistema informado:")

# Cada item da lista tem dois valores. O Python coloca o primeiro
# em 'resto_informado' e o segundo em 'modulo' para exibir cada equação.
for resto_informado, modulo in congruencias:
    print(f"x ≡ {resto_informado} (mod {modulo})")


# Parte B - Etapa 2: verificar se os módulos são coprimos dois a dois.

# "def" cria uma função: um trecho de código que podemos reutilizar.
# Ela recebe dois números, x e y, e devolve o MDC entre eles.
def calcular_mdc(x, y):
    # Aplicamos o Algoritmo de Euclides enquanto o divisor não for zero.
    while y != 0:
        quociente = x // y
        resto = x % y

        # Mostramos cada divisão para explicar como chegamos ao MDC.
        print(f"  {x} = {y} × {quociente} + {resto}")

        # Na próxima divisão, o divisor atual passa a ser o dividendo,
        # e o resto passa a ser o novo divisor.
        x = y
        y = resto

    # Quando y chega a zero, x guarda o último divisor não nulo: o MDC.
    # "return" entrega esse valor a quem chamou a função.
    return x


# Voltamos à margem esquerda: aqui termina a definição da função
# e começa a verificação dos módulos informados pelo usuário.
print("\nVERIFICAÇÃO DOS MÓDULOS")

# Começamos supondo que todos os pares passam no teste.
# Se encontrarmos um único par com MDC diferente de 1, isso muda.
todos_coprimos = True

# i indica a posição do primeiro módulo do par.
for i in range(quantidade):

    # j começa na posição seguinte à de i.
    # Assim, não comparamos um módulo consigo mesmo nem repetimos pares.
    for j in range(i + 1, quantidade):

        # Cada item de "congruencias" é um par (resto, módulo).
        # A posição [0] guarda o resto; a posição [1] guarda o módulo.
        modulo_1 = congruencias[i][1]
        modulo_2 = congruencias[j][1]

        print(f"\nComparando os módulos {modulo_1} e {modulo_2}:")
        mdc = calcular_mdc(modulo_1, modulo_2)
        print(f"MDC({modulo_1}, {modulo_2}) = {mdc}")

        # Se o MDC for maior que 1, os dois módulos têm
        # um divisor comum além de 1 e, portanto, não são coprimos.
        if mdc != 1:
            todos_coprimos = False

# Esta decisão vem depois dos dois laços, quando todos os pares já foram vistos.
if not todos_coprimos:
    print("\nO sistema está fora das condições previstas para esta atividade.")
    # Encerramos antes de aplicar o método que exige módulos coprimos.
    raise SystemExit

print("\nTodos os pares têm MDC igual a 1. Podemos continuar o cálculo.")

# Parte B - Etapa 3: calcular o produto total e os produtos parciais.

print("\nPRODUTO TOTAL DOS MÓDULOS")

# Começamos em 1 porque 1 é o elemento neutro da multiplicação.
# Se começássemos em 0, o produto continuaria sendo 0 em todas as etapas.
N = 1

# Cada item de 'congruencias' tem a forma (resto, módulo).
# O sinal _ indica que, neste cálculo, não precisamos usar o resto.
for _, modulo in congruencias:
    anterior = N
    N = anterior * modulo
    print(f"{anterior} × {modulo} = {N}")

print(f"Produto total: N = {N}")

print("\nPRODUTOS PARCIAIS")
produtos_parciais = []

# Agora que N está completo, percorremos as congruências outra vez.
# O enumerate numera cada uma a partir de 1 para identificar a saída.
for indice, (_, modulo) in enumerate(congruencias, start=1):
    # Dividir N pelo módulo atual deixa o produto de todos os outros.
    # A divisão é exata, por isso usamos // para obter um inteiro.
    Ni = N // modulo

    # Guardamos os resultados na mesma ordem das congruências.
    # Vamos precisar dessa correspondência ao calcular os inversos.
    produtos_parciais.append(Ni)
    print(f"N{indice} = {N} ÷ {modulo} = {Ni}")


# Parte B - Etapa 4: encontrar os inversos modulares.

def encontrar_inverso(numero, modulo):
    # Procuramos um candidato que satisfaça:
    # numero × candidato ≡ 1 (mod modulo).

    # Caso especial: na divisão por 1, todo inteiro deixa resto 0.
    # Essa congruência não restringe x; usamos 0 como representante.
    if modulo == 1:
        print("  Módulo 1: todos os inteiros são congruentes a 0. Usamos 0.")
        return 0

    # Para um módulo maior que 1, basta testar de 1 até modulo - 1.
    # Depois disso, os restos começam a se repetir.
    for candidato in range(1, modulo):
        produto = numero * candidato
        resto = produto % modulo

        # Mostramos cada tentativa para justificar a escolha do inverso.
        print(f"  {numero} × {candidato} = {produto}; resto por {modulo}: {resto}")

        if resto == 1:
            # return devolve o candidato e encerra a busca imediatamente.
            return candidato


print("\nINVERSOS MODULARES")
inversos = []

# Usamos a mesma posição nas duas listas para juntar os valores corretos.
# Na posição 0, por exemplo, temos o produto parcial 35 e o módulo 3.
for i in range(quantidade):
    Ni = produtos_parciais[i]
    modulo = congruencias[i][1]  # Cada congruência é um par (resto, módulo).

    print(f"\nBuscando o inverso de {Ni} módulo {modulo}:")
    inverso = encontrar_inverso(Ni, modulo)

    # Guardamos o inverso para usá-lo no cálculo da solução.
    inversos.append(inverso)
    print(f"Inverso encontrado: {inverso}")

print("\nInversos, na ordem das congruências:", inversos)

# Parte B - Etapa 5: calcular a solução pelo Teorema Chinês do Resto.

print("\nCÁLCULO DA SOLUÇÃO")
soma = 0

# Cada congruência contribui com um termo:
# resto pedido × produto parcial × inverso modular.
for i in range(quantidade):
    resto_pedido, modulo = congruencias[i]
    Ni = produtos_parciais[i]
    inverso = inversos[i]

    # Ni é múltiplo dos outros módulos: para eles, este termo deixa resto 0.
    # No módulo desta linha, Ni × inverso equivale a 1.
    # Assim, o termo contribui exatamente com o resto pedido nesta linha.
    termo = resto_pedido * Ni * inverso
    soma += termo
    print(f"Termo {i + 1}: {resto_pedido} × {Ni} × {inverso} = {termo}")

# O resto da soma por N dá a menor solução não negativa.
x0 = soma % N

print(f"\nSoma dos termos: {soma}")
print(f"x0 = {soma} % {N} = {x0}")

# Somar ou subtrair um múltiplo de N preserva todos os restos.
# Por isso, t pode ser qualquer número inteiro, inclusive zero ou negativo.
print(f"Solução geral: x = {x0} + {N} × t, com t inteiro.")

# Parte B - Etapa 6: testar a solução nas congruências originais.
print(f"\nVERIFICAÇÃO DE x = {x0}")
todas_corretas = True

for resto_pedido, modulo in congruencias:
    resto_obtido = x0 % modulo

    # Escrevemos o resto pedido na faixa de 0 até modulo - 1.
    # Exemplo: pedir resto -1 módulo 5 equivale a pedir resto 4.
    resto_esperado = resto_pedido % modulo

    print(f"{x0} % {modulo} = {resto_obtido} | esperado: {resto_esperado}")

    if resto_obtido != resto_esperado:
        todas_corretas = False

if todas_corretas:
    print("A solução satisfaz todas as congruências.")
else:
    print("A solução não satisfaz todas as congruências.")