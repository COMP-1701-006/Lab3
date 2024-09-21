# Operators and f-Strings

## Objectives
The goals of this lab are to learn about:
- User input
- Data types
- Operators, especially `%` and `//`
- Format output with f-Strings

## Setup
1. As with previous labs, click on the GitHub Classroom link to accept this lab and clone the starter code. (Refer to lab 01 instructions) for a refresher on the cloning/committing/syncing process.
2. Open the folder you just cloned in VS code. 

## Incan Gold
In this week's tutorial, you designed an algorithm for a component of the board game [Incan Gold](https://www.eaglegames.net/Incan-Gold-2018-p/102197.htm). Now, it's time to implement it! Working in your starter code repository, create a file named `lab03.py`.

Referring back to your algorithm solution from the tutorial, implement the following functionality:

1. Prompt the user to enter the number of gems.
2. Prompt the user to enter the number of players.
   > Remember, the `input` function always returns a **string** - you must cast the result to the appropriate data type.
3. Calculate the number of gems received by each player and the number left over.
4. Use [f-Strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) to display the number of gems, players, gems per player, and gems left over.
 
Example of a running program, with **bold text** representing user input:
<pre>
Enter the number of gems: <b>17</b>
Enter the number of players: <b>3</b>

Gems:            17
Players:          3
Gems per player:  5
Gems left over:   2
</pre>

Another example:

<pre>
Enter the number of gems: <b>3</b>
Enter the number of players: <b>4</b>

Gems:             3
Players:          4
Gems per player:  0
Gems left over:   3
</pre>

> Note: to pass the formatting test, your output must be displayed *exactly* as shown. f-strings allow you to display text and numbers with a minimum character width - in this case, 2 spaces for the numbers column and 17 for the text column.

## Running tests
This lab has 3 tests: one for the number of gems per player, one for the gems left over, and one for formatting. **You only need to pass 2 of the 3 tests** to pass the lab. However, GitHub only shows you a green check mark when *all* of the tests are passed. The extra test is provided for an extra challenge.


<br><br>
*This lab adapted from lab exercises by Charlotte Curtis*