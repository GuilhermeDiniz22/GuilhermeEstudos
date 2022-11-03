notas = list(map(int,input("\nDigite as notas : ").strip().split()))        

def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('O aluno tirou', media)
  return media
  
def verificar_aprovacao(media):
  if media >= 6:
    print ("Aprovado")
  else:
    print ('Reprovado')
    
media = calcular_media(notas)    
verificar_aprovacao(media)