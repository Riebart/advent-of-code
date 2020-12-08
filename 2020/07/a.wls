rules = ReadList["input","String"] // Select[#, StringLength[#]>0&]&;

edges = (StringCases[#, {
       RegularExpression["^(.*) bags contain"] -> "$1",
       RegularExpression[" ([a-z- ]*) bag"] -> "$1"
       }] // Thread[#[[2 ;;]] -> #[[1]]] &) & /@ rules // Flatten[#, 1] &;

children = Reap[DepthFirstScan[DirectedGraph[edges], "shiny gold", {"PrevisitVertex" -> Sow}]][[2,1]];

Print[Length[children] - 1]
