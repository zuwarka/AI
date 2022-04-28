DOMAINS
name = string
PREDICATES
parent(name,name)
female(name)
male(name)
brother(name,name)
sister(name,name)
son(name, name)
uncle(name,name)
CLAUSES
male("Вася").
male("Федор").
male("Захар").
female("Маша").
female("Даша").
female("Наташа").
parent("Маша","Даша").
parent("Маша","Наташа").
parent("Даша","Захар").
parent("Наташа","Вася").
parent("Наташа","Федор").
brother("Вася","Федор").
sister("Наташа","Даша").
sister("Даша","Наташа").
son("Федор", "Наташа").
son("Вася", "Наташа").
son("Захар", "Даша").

uncle(X,Y):-parent(Z,Y),sister(Z,W),parent(W,X).
uncle(X,Y):-parent(Z,Y),brother(Z,W),parent(W,X).
GOAL
uncle(X,"Захар").
