# Pet Project for Advanced Software Engineering WS 2018/19

My pet project for Advanced Software Engineering was inspired by a kaggle notebook. It is a Reinforcement Learning program for the game Tic Tac Toe. The program creates a neural network model for turn evaluations and is trained while playing against a programmed opponent. In the end a user can play against the trained model. In this documentation I will show UML diagrams and some metrics for the code, as well as some clean code concepts.

# UML DIAGRAMS

Following UML diagram shows the connection of all modules for the program.

![image](images/UML1.png)

The next diagram shows the user interaction when playing the game.

![image](images/UML2.png)

The third diagram shows the game process as a whole.

![image](images/UML3.png)

# METRICS

Sonarcube performs a scan with three different metrics in Bugs, Vulnerabilities and Code Smells and rates all three categories:
Sonarcube rated the code with an overall rating of A. The scanner found 0 bugs and 0 vulnerabilities. It found some issues in the naming of variables but still gave an A rating in the Code Smells section.
[![sonar cube]( https://sonarcloud.io/api/project_badges/measure?project=Sonar_PetProject&metric=alert_status)](https://sonarcloud.io/dashboard?id=agademic_pet_project_tic)

# TRAVIS CI

[![Build Status](https://travis-ci.org/agademic/pet_project_tic.svg?branch=master)](https://travis-ci.org/agademic/pet_project_tic)

# CLEAN CODE

My clean code principles are based on the 'clean code cheat sheet', which can be found here: [Link](https://www.planetgeek.ch/wp-content/uploads/2013/06/Clean-Code-V2.2.pdf)

[Example 1](https://github.com/agademic/pet_project_tic/blob/master/evaluator_model.py#L15): General and Understandability

[Example 2](https://github.com/agademic/pet_project_tic/blob/master/play.py#L20): High Cohesion

[Example 3](https://github.com/agademic/pet_project_tic/blob/master/game_class.py#L12): Class Design

[Example 4](https://github.com/agademic/pet_project_tic/blob/master/opponent.py#L14): Naming

[Example 5](https://github.com/agademic/pet_project_tic/blob/master/opponent.py#L316): Methods

# DSL

Domain Specific Language does not contibute to my project. A code snipped can be found here: 

# Functional Programming

only final data structures:

(mostly) side effect free functions:

the use of higher order functions:

functions as parameters and return values:

use clojures / anonymous functions:
