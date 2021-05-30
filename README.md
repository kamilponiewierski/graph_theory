# graph_theory

### Format wejscia:
1. Linijka z liczbą wierzchołków grafu
1. x linijek (x - liczba wierzchołków grafu), każda zaczyna się od nazwy wierzchołka, po czym w parach podaje sąsiada i wagę krawędzi
1. Linijka z punktem startowym algorytmu
1. Linijka z wierzchołkiem, do którego ścieżki szukamy

### Analiza algorytmu:
Algorytm rozwiązuje problem znajdowania najkrótszej ścieżki pomiędzy dwoma wierzchołkami grafu.
Przykłady zastosowania obejmują nawigację z użyciem GPS i map -
obliczają najkrótszą - najszybszą - drogę pomiędzy dwoma miejscowościami.

Obecnie do tych celów używa się innych algorytmów (Dijkstra jest od nich wolniejsza),
Google korzysta na przykład z [contraction hierarchies](https://en.wikipedia.org/wiki/Contraction_hierarchies)