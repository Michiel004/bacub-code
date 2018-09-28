-module(machtest).

-export([match/1]).

match(T) -> match(T, []).
match([], Acc) -> lists:reverse(Acc);
match([{a, F}|T], Acc) -> match(T,[{a, F*F} | Acc]);
match([{b, F}|T], Acc) -> match(T, [{b, F+10} | Acc]);
match([{c, _}|T], Acc) -> match(T, [{c, nil} | Acc]).
