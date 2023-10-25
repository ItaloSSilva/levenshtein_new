def distancia_leven(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    
    distancia = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
    for i in range(len_s1 + 1):
        distancia[i][0] = i
    
    for j in range(len_s2 + 1):
        distancia[0][j] = j
    
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            distancia[i][j] = min(
                distancia[i - 1][j] + 1,
                distancia[i][j - 1] + 1,
                distancia[i - 1][j - 1] + cost
            )
            
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                distancia[i][j] = min(distancia[i][j], distancia[i - 2][j - 2] + cost)
    
    return distancia[len_s1][len_s2]

def calculo_distancias(referencia, strings):
    distancias = {}
    for s in strings:
        distancia = distancia_leven(referencia, s)
        distancias[s] = distancia
    return distancias

# Exemplo de uso com uma string de referência e uma lista de strings
referencia_string = "banheiro"
string_lista = ["ciclista", "banheiro", "computador", "carro", "pessoa"]

distancias = calculo_distancias(referencia_string, string_lista)
for s, distancia in distancias.items():
    print(f"Distância entre '{referencia_string}' e '{s}': {distancia}")