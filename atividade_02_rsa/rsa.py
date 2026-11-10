# Portfólio de Estruturas Matemáticas - Parte 2
# Atividade 2: criptografia RSA com números inteiros
# Sinezio Junio Porfirio Araujo | Matrícula: 2212130034
#
# Exemplo para acompanhar os cálculos: p = 5, q = 11, e = 3, M = 7.
# O programa começa a pedir os valores logo depois das funções abaixo.


def ler_inteiro(pergunta):
    # input() lê texto. Se int() não conseguir convertê-lo, pedimos de novo.
    while True:
        try:
            return int(input(pergunta))
        except ValueError:
            print("Digite um número inteiro, sem letras nem casas decimais.")


def eh_primo(numero):
    # Um primo é maior que 1 e tem somente dois divisores positivos: 1 e ele mesmo.
    if numero <= 1:
        print(f"{numero} não é primo: precisa ser maior que 1.")
        return False

    # Basta procurar um divisor até a raiz quadrada. Se numero = a × b,
    # pelo menos um dos fatores é menor ou igual à raiz.
    divisor = 2
    while divisor * divisor <= numero:
        resto = numero % divisor
        print(f"  {numero} % {divisor} = {resto}")
        if resto == 0:
            print(f"{numero} não é primo: é divisível por {divisor}.")
            return False
        divisor += 1

    print(f"{numero} é primo.")
    return True


def calcular_mdc(a, b):
    # Algoritmo de Euclides: os divisores comuns de a e b são os mesmos
    # de b e do resto. Assim podemos trocar o par sem mudar o MDC.
    while b != 0:
        quociente = a // b
        resto = a % b
        print(f"  {a} = {b} × {quociente} + {resto}")
        a = b
        b = resto
    return a  # Último divisor diferente de zero.


def encontrar_inverso(e, phi):
    # Procuramos d de forma direta, como na atividade de congruências.
    # O teste anterior de MDC garante que um dos candidatos vai funcionar.
    for candidato in range(1, phi):
        resto = (e * candidato) % phi
        print(f"  ({e} × {candidato}) % {phi} = {resto}")
        if resto == 1:
            return candidato


def potencia_modular(base, expoente, modulo):
    # Para calcular base elevada ao expoente, multiplicamos pelo mesmo fator
    # em cada etapa. Guardamos só o resto, pois reduzir antes da próxima
    # multiplicação não altera o resto final. Ex.: 7² mod 55 = 49;
    # na terceira etapa, basta calcular (49 × 7) mod 55.
    fator = base % modulo
    resultado = 1
    print(f"  Início: resultado = 1; fator = {base} % {modulo} = {fator}")
    for etapa in range(1, expoente + 1):
        anterior = resultado
        resultado = (anterior * fator) % modulo
        print(f"  Etapa {etapa}: ({anterior} × {fator}) % {modulo} = {resultado}")
    # Se o expoente for zero, não há multiplicações; o resultado é 1.
    return resultado


print("ATIVIDADE 2 - CRIPTOGRAFIA RSA")
print("\nPARTE A - ESCOLHA DOS PRIMOS E DO EXPOENTE PÚBLICO")

while True:
    p = ler_inteiro("Digite o primeiro inteiro (p): ")
    q = ler_inteiro("Digite o segundo inteiro (q): ")
    p_primo = eh_primo(p)
    q_primo = eh_primo(q)

    if not p_primo or not q_primo:
        print("Informe dois números primos.\n")
    elif p == q:
        print("Os primos precisam ser diferentes.\n")
    elif (p - 1) * (q - 1) <= 2:
        # Aqui está o ajuste: 2 e 3 são primos distintos, mas dão φ(n) = 2.
        # Não há um inteiro e estritamente entre 1 e 2. Pedimos outros primos
        # agora para não deixar o usuário preso na escolha de e.
        print("Não existe expoente inteiro entre 1 e φ(n). Escolha outros primos.\n")
    else:
        break

n = p * q
# Esta fórmula para o totiente vale porque p e q são primos distintos.
phi = (p - 1) * (q - 1)
print(f"n = {p} × {q} = {n}")
print(f"φ(n) = ({p} - 1) × ({q} - 1) = {phi}")

while True:
    e = ler_inteiro(f"Digite o expoente público e (1 < e < {phi}): ")
    if not (1 < e < phi):
        print(f"Fora do intervalo: e deve ser maior que 1 e menor que {phi}.")
        continue  # Pede outro e; ainda não é necessário calcular o MDC.

    print("Verificação de e pelo Algoritmo de Euclides:")
    mdc = calcular_mdc(phi, e)
    print(f"MDC({e}, {phi}) = {mdc}")
    if mdc == 1:
        break
    print("Expoente rejeitado. Para ter inverso, e precisa ser coprimo com φ(n).")

print(f"Parâmetros aceitos: p = {p}, q = {q}, n = {n}, φ(n) = {phi}, e = {e}.")

print("\nPARTE B - CONSTRUÇÃO DAS CHAVES")
# d é o inverso de e módulo phi: o produto e × d precisa deixar resto 1.
d = encontrar_inverso(e, phi)
print(f"Verificação de d: ({e} × {d}) % {phi} = {(e * d) % phi}")
print(f"Chave pública (e, n): ({e}, {n})")
print(f"Chave privada (d, n): ({d}, {n})")

print("\nPARTE C - CIFRAGEM E DECIFRAGEM")
while True:
    mensagem = ler_inteiro(f"Digite a mensagem inteira M (0 ≤ M < {n}): ")
    if 0 <= mensagem < n:
        break
    print(f"Escolha um inteiro de 0 até {n - 1}.")

# A chave pública cifra; a chave privada recupera o número original.
print(f"Cifragem: C = {mensagem}^{e} mod {n}")
cifra = potencia_modular(mensagem, e, n)
print(f"Decifragem: M' = {cifra}^{d} mod {n}")
recuperada = potencia_modular(cifra, d, n)
print(f"Original: {mensagem} | Cifrado: {cifra} | Decifrado: {recuperada}")
if recuperada == mensagem:
    print("Conferência: o número decifrado é igual ao original.")
else:
    print("Conferência: o número decifrado é diferente do original.")

print("\nPARTE D - TEOREMAS DE EULER E FERMAT")
print(f"Condição de Euler: calcular o MDC entre {mensagem} e {n}.")
mdc_mensagem = calcular_mdc(n, mensagem)
print(f"MDC({mensagem}, {n}) = {mdc_mensagem}")

# Euler: M^φ(n) deixa resto 1 SOMENTE SOB A HIPÓTESE de M coprimo com n.
# Para mostrar a redução do expoente, usamos φ(n) + 1: ele se reduz a 1.
if mdc_mensagem == 1:
    print(f"Euler se aplica: calculando {mensagem}^{phi} mod {n}.")
    valor_euler = potencia_modular(mensagem, phi, n)
    print(f"{mensagem}^{phi} mod {n} = {valor_euler} (esperado: 1).")
    print(f"Portanto, {mensagem}^({phi} + 1) mod {n} = "
          f"({valor_euler} × {mensagem}) mod {n} = {(valor_euler * mensagem) % n}.")
else:
    print("Euler não permite reduzir o expoente neste caso: o MDC não é 1.")
    print("A cifragem e a decifragem acima usaram reduções a cada multiplicação.")

# Fermat exige um módulo PRIMO. Por isso usamos p, não o módulo composto n.
# Se p dividir M, usamos q como base da demonstração. Como p e q são
# primos distintos, q nunca é divisível por p. A mensagem original não muda.
base_fermat = mensagem
if base_fermat % p == 0:
    print(f"{p} divide {mensagem}. Para demonstrar Fermat, usamos a base q = {q}.")
    base_fermat = q

print(f"Condições de Fermat: {p} é primo e {base_fermat} % {p} = {base_fermat % p}.")
valor_fermat = potencia_modular(base_fermat, p - 1, p)
print(f"{base_fermat}^({p} - 1) mod {p} = {valor_fermat} (esperado: 1).")
print(f"Assim, para esta base e o módulo {p}, o expoente pode ser reduzido módulo {p - 1}.")
