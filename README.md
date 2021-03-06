# graph_theory

### Format wejscia:
1. Linijka z liczbą wierzchołków grafu
1. x linijek (x - liczba wierzchołków grafu), każda zaczyna się od nazwy wierzchołka, po czym w parach podaje sąsiada i wagę krawędzi
1. Linijka z punktem startowym algorytmu
1. Linijka z wierzchołkiem, do którego ścieżki szukamy


### Instrukcja obsługi
Najłatwiej przekierować plik in.txt na wejście, można też manualnie wpisać graf zgodnie z instrukcjami konsoli

### Analiza algorytmu:
Algorytm rozwiązuje problem znajdowania najkrótszej ścieżki pomiędzy dwoma wierzchołkami grafu.
Przykłady zastosowania obejmują nawigację z użyciem GPS i map -
obliczają najkrótszą - najszybszą - drogę pomiędzy dwoma miejscowościami.

Obecnie do tych celów używa się innych algorytmów (Dijkstra jest od nich wolniejsza),
Google korzysta na przykład z [contraction hierarchies](https://en.wikipedia.org/wiki/Contraction_hierarchies),
być może [A*](https://en.wikipedia.org/wiki/A*_search_algorithm)
lub usprawnionych wersji Dijkstry, na przykład przegląda się graf z obu stron - ze startu i końca,
tak żeby spotkały się w okolicach środka, albo dzieli graf na warstwy - autostrad, dróg głównych,
i tak dalej, do dróg lokalnych.