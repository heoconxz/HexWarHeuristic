# CSCI 564 - Fall 2021 Project: HexWar
 
## Background


Hex is a connection game. The game can never end in a draw (tie), in other words, Hex is also a "determined game".

Hex is a finite, perfect information game, and an abstract strategy game that belongs to the general category of connection games. Hex is a special case of the "node" version of the Shannon switching game.

As a product, Hex is a board game; it may also be played with paper and pencil.

John Nash was the first to prove that Hex cannot end in a draw, a non-trivial result colloquially called the "Hex theorem."

In 1976, Shimon Even and Robert Tarjan proved that determining whether a position in a game of generalized Hex played on arbitrary graphs is a winning position is PSPACE-complete.

Due to the simplicity of the rules and its computation hardness, Hex is a very popular adversarial game in Artificial Intelligence.


## Problem

A Hex game follows simple rules:

* Each player plays one after the other by placing a coloured hex on the board.
* The first to connect the two sides of his colour win.
* You cannot play on a player tile.

## Algorithms and Heuristics

An adversarial game where two or more players plays against each other. These types of games are very hard to solve due to their combinatorial explosion.

To solve this issue, AI researcher came up with a search algorithm combined with a heuristic function.
The search algorithm will explore the tree of the possibilities to evaluate what is the best move to execute. As the number of future possible moves is too large, the heuristic function will help to search only in relevant part of the tree.

Depending on the type of algorithm, the heuristic function can change a lot.
Good heuristic functions are not trivial to find, it requires expert knowledge.

Regarding the Hex game, there are different approaches. To give you somewhere to start I will give you two common approaches:

* Minimax algorithm combined with a heuristic evaluating the quality of the move
* Approach based on pattern recognition.
