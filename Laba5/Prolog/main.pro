domains
L = integer*
predicates
increm(L,integer,integer,integer,L,L)
append(L,L,L)
clauses
append([],L,L):-!.
append([H|T],P,[H|Y]):-append(T,P,Y).
increm([],_,_,_,L,L):-!.
increm([H|T],Index,N,I,L,Lanother):- Index<>I,Index1=Index+1, append(L,[H],L2),increm(T,Index1,N,I,L2,Lanother).
increm([H|T],Index,N,I,L,Lanother):-H1=H+N,Index1=Index+1,append(L,[H1],L2),increm(T,Index1,N,I,L2,Lanother).
goal
increm([1, 2, 3, 4, 5, 6, 7, 8],0,-5,2,[],List3),write(List3),nl.
