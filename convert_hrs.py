def entrada():
    hora = float(input('Digite a hora no formato (hh:mm):'  ).replace(':','.'))
    return hora

def conversor_horas():
    time = entrada()
    minutos = time * 60
    print(f'Hora convertida em minutos: {int(minutos)}')
    return minutos

def conversor_minutos():
    minutos_hora = conversor_horas()
    segundos = minutos_hora * 60
    print(f'Hora convertida em segundos: {int(segundos)}')

conversor_minutos()





