predicates
prosmotr(char,string)
meetin(string,string,string)
clauses
prosmotr(_,"") :- fail.
prosmotr(C,S) :- frontchar(S,C,_),!.
prosmotr(C,S) :- frontchar(S,_,RS),prosmotr(C,RS).
meetin("",_,"").
meetin(A,B,R) :- frontchar(A,A1,RA), prosmotr(A1,B), meetin(RA,B,RR), frontchar(R,A1,RR), !.
meetin(A,B,R) :- frontchar(A,_,RA), meetin(RA,B,R).
goal
meetin("Пенза","пемза",R),write(R),nl.
