# Assignment 3 Part 1: World Building

This assignment is entirely about representing the world.

You are going to represent two problems (Tower of Hanoi and the 8-Puzzle) for which you will need to represent both the state of the world and the rules that govern whether or not you can take actions. This will be very much like what we did in class for the Tower of Hanoi.

You will need to figure out:

* What are the objects?  
* What are the relationships?  
* What are the inferences that I can draw about the world itself?  
* How do I represent the constraints (rules) of the problem?  

## The Tower of Hanoi

![A game state of the Tower of Hanoi](/images/th.png)

**Objects**: Disks, Pegs, Base  
**Relationships**: disks are on pegs, disks are larger than other disks, disks are on top of other disks, pegs can be empty, there is a disk at the top of any stack.  
**Inferences**: If you are larger than another disk and it is larger than a third, you are larger than it too.  
**Constraints**: A disk can be moved to a peg if it is on the top of a stack and either the peg is empty or the disk at the top of the stack on the peg is larger than it is.  

The two predicates that you have to use are `ON` for the location of disks on pegs and `MOVABLE` for the moves that can be taken. 
* `ON` should take two arguments `?disk ?peg`
* `MOVABLE` should take three `?disk ?initial ?target`

You need to build three KBs, each with five disks: 

1. One with all of the disks on the first peg.  
2. One with the two smallest disks on the last peg and the others on the first.
3. One with the smallest disk on the last peg, the second smallest on the second peg, and the others on the first peg.

We will test your setup by checking whether you have the correct `ON` and `MOVABLE` Facts. 

## The 8-Puzzle

![Game states of the 8-Puzzle](/images/p8.png)

In the 8-Puzzle, you move around tiles until they are in the target configuration.  

You need to be able to represent the tiles and their locations.  The tiles will each have their own names and the locations should probably be captured via X/Y coordinates. You need to represent the `empty` space as well with its own name and location. Note that in the starter code, the Y axis stretches from the top to the bottom of the screen. 

You can only move a tile to an empty space if it is adjacent to it.  This argues for the needs for a predicate that represents adjacency.  We are not going to do math in FOPC for this assignment, so I am going to give you a trick.  

**Trick**: In this game, two tiles A and B are adjacent if they:  
1. share the X coordinate or the Y coordinate, and  
2. either A or B has the value 2 on the coordinate they do not share.  
This ends up being four rules for adjacency.  

A tile at (1,1) is adjacent to a blank at (1,2) or (2,1). Adjacency is about the only inference you have to make for this in terms of the description of the world.  

You will still have to represent `MOVABLE`. A tile is `MOVABLE` if it is adjacent to the blank (`empty`).  As with the Tower of Hanoi, `MOVABLE` has to have a specific form (for testing purposes):
* `MOVABLE` should take five arguments `?piece ?initialX ?initialY ?targetx ?targety`.  

You need to build two KBs:

1. One with the layout shown on the left side of the image above.
2. One with the layout shown on the right side of the image above.

We will test your setup by checking whether you have the correct `MOVABLE` Facts. 


## Starter Code

This starter code builds on top of the solution code of Assignment 2. `kb_and_inference_engine.py` contains the definition of a KnowledgeBase (KB) and an InferenceEngine, similar to what you have implemented for Assignment 2. `game_masters.py` contains simple game masters that keep track of the states of each game with KBs -- you do not need to worry about them for this Part of the assignment (Assignment 3 Part 1). 

The `flatfiles` directory contains five empty flat files that you will fill with facts and rules -- text representations that must be parsable to Fact and Rule objects. The provided test cases in `main.py` will be similar to the tests that we will use to grade your work. 

Each test in `main.py` automatically loads one of the flat files, assert all of its facts and rules to a game master, and check if the resulting KB of the game master describes the desired game state. 

## Your Tasks

For this assignment, you will populate the files included in the `flatfiles` directory with facts and rules, so that the facts and rules correctly represent the five desired game states (three from the Tower of Hanoi and two from the 8-Puzzle). The name of each file indicates which state of which game you should represent. 

## Preview: Part 2

The work that you do for this assignment will also be used in the next assignment (will be released this Friday). Good Rule design (as in the KB context and not the game rules) in this assignment could make maintaining game states, an important matter for the next assignment, easier and less error-prone. 
