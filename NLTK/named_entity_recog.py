import nltk
import numpy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

x = "Estamos com diversas oportunidades para Desenvolvedores! Se você: Possui conhecimento em desenvolvimento e modelagem de dados; Quer atuar em projetos com tecnologias diversas como Java, Ruby e PHP; Tem paixão por aprender e quer participar ativamente das decisões dos produtos e projetos; Pesquisa e aplica novas tecnologias em projetos, implementa processos e recomendação de ferramentas; Respira e valoriza código limpo e testes automatizados; Tem vontade de participar ativamente das decisões de produto, cerimônias do SCRUM, definição de arquitetura e melhoria contínua. E se pessoalmente: Quer trabalhar com propósito de impactar milhares pessoas através da educação; Tem um mindset de melhoria contínua e trabalho em equipe; Trabalha com autonomia e responsabilidade, participando ativamente das decisões do produto; E se sente motivado(a) em um ambiente descontraído. Aqui é o seu lugar! O Escritório é em Botafogo e você pode trabalhar de bermuda, jogar ping pong e fliperama!"

def pre_process(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    np_rule = 'NP: {<DT>?<JJ>*<NN>}'

    cp = nltk.RegexpParser(np_rule)
    cs = cp.parse(sent)
    print(cp)
    return sent

print(pre_process(x))
print(nltk.sent_tokenize(x))


