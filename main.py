
import random

#------ FUNZIONI ------
def complementario(seq_DNA):
    # Inicializamos una lista vacía para la secuencia de ADN complementaria.
    seq_DNA_complementaria = []
    for base in seq_DNA:
        if base == 'A':
            seq_DNA_complementaria.append('T')
        elif base == 'T':
            seq_DNA_complementaria.append('A')
        elif base == 'C':
            seq_DNA_complementaria.append('G')
        elif base == 'G':
            seq_DNA_complementaria.append('C')
    return ''.join(seq_DNA_complementaria)

## GENERATIÓN (Lo mismo que el primer trabajo)
# Primero necesitas generar una secuencia de ADN aleatoria.
def generation(length_S):
    # Implementamos todas las diferentes bases.
    Bases_DNA = ['A', 'T', 'C', 'G']
    random_sequence = ''.join(random.choice(Bases_DNA) for _ in range(length_S - 6))
    return random_sequence

def dividere_sequenza_dna(seq_DNA):
    index_tac = seq_DNA.find(input(""))
    if index_tac != -1:
        parte_dopo = seq_DNA[index_tac + 3:]
        return parte_dopo
    else:
        return None

#Complemento la nueva secuencia
def complementario2(seq_DNA_N):
    seq_DNA_complementaria_N = []
    for base in seq_DNA_N:
        if base == 'A':
            seq_DNA_complementaria_N.append('T')
        elif base == 'T':
            seq_DNA_complementaria_N.append('A')
        elif base == 'C':
            seq_DNA_complementaria_N.append('G')
        elif base == 'G':
            seq_DNA_complementaria_N.append('C')
    return ''.join(seq_DNA_complementaria_N)


#------ CLASSI AUTO E MANUALE ------

# Elección del tipo de generación
class ClaseA:
    def avvio(self):
        print("\nGeneración automático de la secuencia de ADN")

        # Por conveniencia elijo una longitud de 24 bases.
        length_S = 275
        seq_DNA = generation(length_S)

        # Generamos la secuencia complementaria.
        seq_DNA_complementaria = complementario(seq_DNA)

        # Imprimimos la secuencia de ADN original.
        print("\nSecuencia de ADN generada:")
        print(seq_DNA)
        print(seq_DNA_complementaria)

        #Corté la secuencia con un primer
        print("\nIntroduzca la secuencia de bases correspondiente al cebador: ")

        #seq_DNA_N = dividere_sequenza_dna(seq_DNA)
        seq_DNA_N=seq_DNA
        index_tac = seq_DNA.find(input(""))

        if index_tac != -1:
            parte_dopo = seq_DNA[index_tac + 3:]
            seq_DNA_complementaria_N = complementario2(seq_DNA_N)
            print("\nLa doble hélice después del corte será:")
            print(seq_DNA_N)
            print(seq_DNA_complementaria_N)

            #Separo las hélices
            print("\nEntonces se produce la separación de las dos hélices:")
            print("\nHélice superior")
            print(seq_DNA_N)
            print("\nHélice inferior")
            print(seq_DNA_complementaria_N)
            print("\nY finalmente ocurre la duplicación:")
            print("\nPrimera hélice duplicada")
            print(seq_DNA_N)
            print(seq_DNA_complementaria_N)
            print("\nSegunda hélice duplicada")
            print(seq_DNA_complementaria_N)
            print(seq_DNA_N)

        else:
            print("Elección no válida")

class ClaseB:
    def avvio(self):
      DNA = input("\nIntroduzca la secuencia de ADN (solo una hélice) : ")
      seq_DNA = DNA

        # def insertar():
        #     # Pida al usuario que ingrese una secuencia de ADN
        #     DNA = input("\nIntroduzca la secuencia de ADN (solo una hélice) : ")
        #     return DNA

        #seq_DNA = insertar()

      # Verifique que la secuencia de ADN sea válida (que consta únicamente de A, C, G, T)
      valid_chars = "ACGT"
      if all(base in valid_chars for base in DNA):
          print("\nHélice insertada:", DNA)
          seq_DNA_complementaria = complementario(seq_DNA)

          # Imprimimos la secuencia de ADN.
          print("\nSecuencia de ADN insertada:")
          print(seq_DNA)
          print(seq_DNA_complementaria)

          # Corté la secuencia con un primer
          print("\nIntroduzca la secuencia de bases correspondiente al cebador: ")

          def dividere_sequenza_dna(seq_DNA):
              index_tac = seq_DNA.find(input(""))
              if index_tac != -1:
                  parte_dopo = seq_DNA[index_tac + 3:]
                  return parte_dopo
              else:
                  return None

          seq_DNA_N = dividere_sequenza_dna(seq_DNA)

          seq_DNA_complementaria_N = complementario(seq_DNA_N)

          # Separo las hélices
          print("\nEntonces se produce la separación de las dos hélices:")
          print("\nHélice superior")
          print(seq_DNA_N)
          print("\nHélice inferior")
          print(seq_DNA_complementaria_N)

          # Duplicación
          print("\nY finalmente ocurre la duplicación:")
          print("\nPrimera hélice duplicada")
          print(seq_DNA_N)
          print(seq_DNA_complementaria_N)
          print("\nSegunda hélice duplicada")
          print(seq_DNA_complementaria_N)
          print(seq_DNA_N)

      else:
          print("La secuencia de ADN contiene caracteres no válidos.")
          #breakpoint()



#------- LOOP -------

# Pide al usuario que seleccione una clase.
print("Elegir el tipo de generación del ADN:")
print("\n1. Generación automático")
print("2. Generación manual")

# Funzione per selezionare una delle tre classi e invocare il metodo di avviso
def elección_generación(número1):
    if número1 == 1:
        clase = ClaseA()
    elif número1 == 2:
        clase = ClaseB()
    else:
        print("Elección no válida")
        return
    clase.avvio()

try:
    número_1 = int(input("\nIntroduce tu número de clase: "))
    elección_generación(número_1)
except ValueError:
    print("Por favor ingrese un número valido.")