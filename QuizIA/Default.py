#coding: utf-8

q1 = 'A IA fraca estuda a solução de problemas complexos?'
q2 = "Para transportar os três discos empilhados de um poste para um poste vizinho do problema das torres de Hanói, a quantidade mínima de passos é 12? "
q3 = "A quantidade de estados do jogo da velha que garantem a vitória do jogador X na sua próxima jogada, independente da jogada que fizer o jogador O é 8 ? "
q4 = "Nos anos 60 Alan Turing publicou o artigo Computing Machinery & Intelligence ?"
q5 = "Segundo a filosofia a IA é um dom divino que nos torna semelhantes ao criador?"

qs = [q1,q2,q3,q4,q5]

ans = ['f','f','f','f','f']

ops= "V (verdadeiro) F (Falso) :> "

nota= 0
r = ''
for q in qs:
    for an in ans:
        if(an == input(q+" "+ ops)):
            nota+=1



print("Nota:"+(nota*2))
