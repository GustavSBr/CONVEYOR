def main():    
    while True:
        try:
            conveyor = int(input("Quantidade de conveyors: "))
            posto = int(input("Quantidade de postos: "))
            break
        except ValueError:
            print("Erro")
    base = posto + 2
    tampa = posto + 2
    verde = conveyor
    vermelho = posto + conveyor + 3
    amarelo = posto + 3
    giroflex = conveyor
    emergencia = round(posto + conveyor + (posto + conveyor) * 3 )
    plaqueta_emergencia = emergencia
    knob = round(posto + conveyor + (3 / 100))
    bloco_NA = round(knob + emergencia + (5 / 100))
    caixa_3072 = posto
    caixa_3073 = giroflex
    fim_de_curso = round((posto / 2) / 3 + (5 / 100))
    cabo_manga = round(posto * 1.5 + 6 )   

    print(f"Base: {base}")
    print(f"Tampa: {tampa}")
    print(f"Verde: {verde}")
    print(f"Vermelho: {vermelho}")
    print(f"Amarelo: {amarelo}")
    print(f"Giroflex: {giroflex}")
    print(f"Emergencia: {emergencia}")
    print(f"Plaqueta Emergencia: {plaqueta_emergencia}")
    print(f"Knob: {knob}")
    print(f"Bloco NA: {bloco_NA}")
    print(f"Caixa 3072: {caixa_3072}")
    print(f"Caixa 3073: {caixa_3073}")
    print(f"Fim de Curso: {fim_de_curso}")
    print(f"Cabo Manga: {cabo_manga}")
    
    input("aperte 'enter' para fechar")

if __name__ == "__main__":
    main()
