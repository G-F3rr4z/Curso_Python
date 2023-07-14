# Closure e funcoes que retornam outras funcoes

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# print(falar_bom_dia('Gabriel'))
# print(falar_boa_noite('Gabriel'))


for nome in ['Maria', 'Joana', 'Gabriel']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))



    
# return falar_bom_dia(nome)