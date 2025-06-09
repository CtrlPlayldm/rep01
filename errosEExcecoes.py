#print('Ctrl+Play)

#print("O que acontece se você passar o valor 0 para o segundo argumento de int()?")
#x = input('Digite um numero: ')
#y = input('Digite outro numero: ')

#print(int(x)/int(y))



def perguntaNumero():
  numero = 1
  while True:
    try:
      val = int(input("Digite um número inteiro: "))
    except:
      print("Parece que você não digitou um número inteiro!")
      continue
    else:
      print("Obrigado por digitar um número inteiro!")
      break
    finally:
      print(f"Tentativa número: {numero}")
      numero += 1
  print(val)

perguntaNumero()