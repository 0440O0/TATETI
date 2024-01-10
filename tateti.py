#dimensiones de tablero
print('Cantidad de filas y columnas del tablero:')
n=int(input())
T=[]

#funciones
def mostrar_M():
    for i in range(n):
        print()
        for g in range(n):
            if g==(n-1):
                print(T[i][g], end=' ')
            else:
                print(T[i][g], end=' | ')

def elegir_lug(jugador):
    print(f'\nTURNO DE {jugador.nombre.upper()}:')
    print('fila:')
    f=int(input())
    print('columna:')
    c=int(input())

    while T[f-1][c-1]=="X" or T[f-1][c-1]=="O":
        print('\nElija un lugar que no este ocupado :)')
        print('fila:')
        f=int(input())
        print('columna:')
        c=int(input())
    
    T[f-1][c-1]=jugador.signo
    return jugador.nombre
    
def ganador(nom):
    d=0
    for i in range(n-1):
        for j in range(n-1):
            if i==j and (T[i][j]==T[i+1][j+1] and (T[i][j] =='X' or T[i][j] =='O')):
                d+=1
    if d==(n-1):
        print(f'\n{nom.upper()} GANA!!!')
        return 0
    
    for i in range(n):
        c=0
        for j in range(n-1):
            if T[j][i]==T[j+1][i] and (T[j][i] =='X' or T[j][i] =='O'):
                c+=1

        if c==(n-1):
            print(f'\n{nom.upper()} GANA!!!')
            return 0
    
    for i in range(n):
        f=0
        for j in range(n-1):
            if T[i][j]==T[i][j+1] and (T[i][j] =='X' or T[i][j] =='O'):
                f+=1
        if f==(n-1) or c==(n-1):
            print(f'\n{nom.upper()} GANA!!!')
            return 0
        else:
            return 1
            
    

for i in range(n):
    T.append(['-']*n)


print()
class jugador:
    def __init__(self,turno,nombre,signo):
        self.turno=turno
        self.nombre=nombre
        self.signo=signo


print('----------------------------------------')

jugador_1= jugador(1,nombre=input('Como se llama el jugador 1?\n'),signo=input('X o O?\n'))

if (jugador_1.signo).lower() != 'x' and (jugador_1.signo).lower() != 'o':
    print('Ingreso un valor invalido, su marca por default es: "X"')
    jugador_1.signo="X"
print('----------------------------------------')
if (jugador_1.signo).lower()=='x':
    jugador_2= jugador(2,nombre=input('Como se llama el jugador 2?\n'),signo='O')
else:
    jugador_2= jugador(2,nombre=input('Como se llama el jugador 2?\n'),signo='X')

fin=1
mostrar_M()
while fin==1:
    #turno jugador 1
    nom=elegir_lug(jugador_1)
    mostrar_M()
    fin=ganador(nom)
    if fin==0:
        break
    #turno jugador 2
    elegir_lug(jugador_2)
    mostrar_M()
    fin=ganador(nom)


#FIN :) -----> SUBIR A GIT HUB
    
