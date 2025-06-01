# Tactego

Tactego Game
A Python implementation of a strategic two-player board game similar to Stratego, where players attempt to capture their opponent's flag while protecting their own.
Author Information

Author: Timothy Rauck
Date: November 15, 2023

Game Overview
Tactego is a turn-based strategy game where two players (Red and Blue) battle on a customizable grid board. Each player controls an army of pieces with different ranks and special abilities. The objective is to capture the opponent's flag while strategically positioning your own pieces.
Features

Customizable Board Size: Set your own board dimensions
Random Piece Placement: Pieces are shuffled for each game
Turn-Based Gameplay: Alternating moves between Blue and Red players
Multiple Piece Types: Various ranks and special pieces (Flag, Mines, Scouts, Assassins)
Combat System: Higher-ranked pieces defeat lower-ranked ones
Special Rules: Unique interactions for mines, scouts, and assassins

Prerequisites

Python 3.x
A pieces configuration file (e.g., basic.pieces)

Installation

Clone this repository or download the tactego.py file
Ensure you have a pieces configuration file in the same directory
Run the game using Python

Usage
python tactego.py
Game Setup Prompts
When you start the game, you'll be prompted for:

Random Seed: Enter any string to seed the random number generator
Pieces Filename: Name of your pieces configuration file (e.g., basic.pieces)
Board Length: Number of rows for the game board
Board Width: Number of columns for the game board

Minimum Board Sizes:

basic.pieces: 10x10

small_game.pieces: 4x4

assassin.pieces: 4x4

Pieces Configuration File Format
Create a text file with piece types and quantities:
F 1    # Flag (1 piece) |
M 3    # Mines (3 pieces) |
S 2    # Scouts (2 pieces) |
A 1    # Assassin (1 piece) |
1 2    # Rank 1 pieces (2 pieces) |
2 3    # Rank 2 pieces (3 pieces) |

How to Play

Game Setup

Red pieces are placed on the top rows of the board
Blue pieces are placed on the bottom rows of the board
Pieces are randomly shuffled and distributed

Turn Structure

Blue Player goes first
Players alternate turns
On each turn, select a piece to move by entering its position (row column)
Then select where to move it (row column)

Movement Rules

Most pieces can move one square horizontally or vertically
You cannot move Flags (F) or Mines (M)
You cannot move to the same position
You cannot attack your own pieces

Combat System

When a piece moves to a square occupied by an enemy piece, combat occurs
Higher-numbered pieces defeat lower-numbered pieces
Special piece interactions:

Assassins (A): Always win attacks and always loses defense
Flag (F): Capturing the enemy flag wins the game



Winning Conditions

Capture the opponent's Flag
Some special combat situations may end the game

Game Controls
Input Format

Positions are entered as: row column (e.g., 2 3)
Coordinates start from 0

Example Turn
Blue Player, Select Piece to Move by Position >> 4 2
Blue Player, Select Position to move Piece >> 3 2
