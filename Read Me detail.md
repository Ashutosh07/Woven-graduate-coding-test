**Detailed Information for Approach**

This is a testing task given where I had to develop a CLI appication to parse the input commands and display the result as required.
In this production I was given a robot that can receive commands in order to move it.  These commands will tell the robot to go forwards or backwards, and turn left or right.  These commands would be  in the format <command><number>. Command for direction and number for distance(number of units) moved. 

**### Available commands:**
* `F` - move forward 1 unit
* `B` - move backward 1 unit
* `R` - turn right 90 degrees
* `L` - turn left 90 degrees

Here with my previous knowledge and expertise in Python language I formulated the code in the same.
`Important note:`I have tried to visualise this as a two axis coordinate system namely x and y where x denotes right and left distance and y denoted forward and backward distance that is travelled by the robot.

**`Steps:-`**
*At the very start just for initialization I started off with two points on the coordinate axis(namely x and y) both as (0,0) as initial starting points for the robot.
*I went on with intial import statemnts where i imported two packages namely re(regular expression) and math(for basic mathematics)  
*Then i went to take inputs from the run time interface which would be provided by the user in the system
*After which i took the inputs and split them with a comma delimiter(,) as individual strings and gathered them into a list
*Next I wanted to find the distance travelled in units through each command and So, I segregated each individual command given into string literals(for direction) and number present(for distance).
*I merged all numeral units into a list of strings and converted it to an integer list
*Next i took a loop that traverses through all the given inputs from the list and adds or subtracts the distance tarversed.
*At the end to gain the final distance I did sqare rooted sum of square roots of both x and y which is the formula for absolute distance on a plain; which in turn gives the final result of output i.e. "the minimum amount of distance to get back to the starting point:" which is 4.

Thank you,
Ashutosh
