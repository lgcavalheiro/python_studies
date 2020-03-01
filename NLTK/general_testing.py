import nltk
import numpy
import spacy_udpipe
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import json


x = "Pré-requisitos:- Experiências/conhecimentos necessários: Linguagens de programação: .NET Framework 4.0 ou superior, ASP.NET MVC, HTML 5, CSS 3, Java Script, jQuery, JSON, TDD/BDD/DDD, Web Api e WCF, VS 2013 ou superior, .NET CORE, NODE, ASP Classic, Angular Linguagens dos BD Oracle e SQL Server Arquitetura de software Melhores práticas de desenvolvimento Application Lifecycle Management (ALM) Metodologias ágeis Em infraestrutura e arquitetura de sistemas distribuídos Conhecimento para solução de problemas de performance e erros sistêmicos Principais responsabilidades: Conduzir os desenvolvimentos sob a sua responsabilidade Participar das discussões internas para a busca de soluções técnicas Conduzir o desenvolvimento e abrangência dos testes automatizados Fomentar novas tecnologias e novas abordagens de desenvolvimento"

def pre_process(sent):

    #spacy_udpipe.download("pt")
    model = spacy_udpipe.load('pt')
    sent = model(sent)

    sent = [(t.text, t.pos_) for t in sent]
    
    """ for token in doc:
        print(token.text, token.lemma_, token.pos_, token.dep_) """
    """ stopwords = nltk.corpus.stopwords.words('portuguese')
    sent = [word for word in sent.split() if word not in stopwords]
    sent = str(sent)
    sent = nltk.word_tokenize(sent, language='portuguese')
    sent = nltk.pos_tag(sent, lang='portuguese')
    
    res = []
    print(nltk.help.upenn_tagset('DT'))
    for pair in sent:
        if pair[1] in ['NNP', 'FW', 'CD']:
            res.append(pair) """
    
    np_rule = "CHUNK: {<PROPN>?<PROPN>*<NUM>*}"
    cp = nltk.RegexpParser(np_rule)
    cs = cp.parse(sent)
    return cs

def write_to_json(data_dict):
    with open(f"{console_caller}_analyzed_results.json", "w") as outfile:
        json.dump(data_dict, outfile, indent=4, ensure_ascii=False)

thing = pre_process(x)
write_to_json(thing)
#print(nltk.help.upenn_tagset('NN'))