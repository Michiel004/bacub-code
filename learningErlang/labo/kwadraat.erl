-module(kwadraat).
-export([return/1,reverse/1]).

return(L) -> return(L,[]).
return([],Acc) -> Acc;
return([H|T],Acc)->return(T,[H*H|Acc]). 
reverse(Acc) -> lists:reverse(Acc).
