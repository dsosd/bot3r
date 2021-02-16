# Overview

The strategy implemented is simplistic, yet produces nice results. Due to language limitations, we did not attempt to use a model with any training.

# Strategy

The move is chosen based on three heuristics, in a first-come first-served manner.

The first heuristic is to choose a pocket that gives us an extra turn. If there are multiple pockets that do this, choose the one closest to our store.

The second heuristic is to choose a pocket that allows us to capture the opponent's highest value pocket (ties broken by least "intrusion" into opponent pockets). If multiple pockets satisfy this, choose the one closest to our store.

The third heuristic is to choose a pocket that is closest to our store.

# Results

We implemented the controller in order to test this strategy against three other strategies: random, head, and tail. Random chooses its moves randomly. Head chooses the pocket closest to its store. Tail chooses the pocket furthest from its store.

As the first player, the strategy wins with a margin of ~20 against random and tails, wins with a margin of 10 against itself, and loses to heads with a margin of 4.

As the second player, the strategy wins with a margin of ~18 against random and heads, loses to tails with a margin of 8, and loses to itself with a margin of 10.

# Code

config.py - global config for the game
engine.py - controller for Mancala (Kalah variant)
head_player.py - head strategy
main_player.py - submitted strategy
random_player.py - random strategy
tail_player.py - tail strategy
test.py - used for verification of engine correctness
transform.py - utilities to translate between the engine's and the spec's implementations