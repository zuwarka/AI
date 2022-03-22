predicates
nondeterm sect(integer, integer, integer, integer, string).
clauses
sect(A, B, C, D, S):-B=D,S="The section is parallel to OX".
sect(A, B, C, D, S):-A=C,S="The section is parallel to OY".
sect(A, B, C, D, S):-B=0,D=0,S="The section is belong to OX".
sect(A, B, C, D, S):-A=0,C=0,S="The section is belong to OY".
sect(A, B, C, D, S):-A<>C,B<>D,S="The section is not belong nor OX, nor OY".
goal
sect(0, 0, 0, 6, Z).
