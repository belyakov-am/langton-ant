# langton-ant

Implementation of basic algorithms and environment for launching Langton's Ant with rule RRL on random coloured grids. 

## Intro 
For getting more acquainted with Langton's and, check [wikipedia](https://en.wikipedia.org/wiki/Langton%27s_ant)
In this project rule RRL was observed. Ant begins to build a highway from 40th step with period 18.

## Tasks
1. For each step of period of highway develop and implement an algorithm that determines whether ant will start highway or not
2. Implement an algorithm that determines the moment of entering a highway from current position with determining moment of a highway
3. Randomly colour square; for each ant's launch record the moment of entering a highway, ant's trajectory beyond the square that leads to this highway. Collect statistics for various initial grids. 

## Collecting statistics 
For tracking ant's trajectories outside the square script saved the picture of ant's path each time, when ant came back to square after going beyond square. 

The square with size 3x3 was analyzed. Ant was launched 2.5 * 10^5 times and 3 most frequent patterns were taken.

## Notes to pictures below
0 - white colour, 1 - blue colour, 2 - lilac colour

First big picture in each case depicts initial colouring.  
`Moment of highway` is an iteration of cycle when ant begins to build a highway.  
`Highway started out of/in square` is self-describing. If highway started beyond the square, horizontal and vertical lengths from the closest side of square are mentioned.  
`Frequency of pattern` is also self-describing.

After, there are several pictures with traces of ant beyond the square. Worth mentioning that inside the square the initial colouring is saved for more convenient analysis. 

Last picture depicts the trace of ant after entering highway.

## Pictures with statistics

First case

![First case](../master/pictures/ant-1-1.png)

Second case

![Second case](../master/pictures/ant-1-2.png)

Third case

![Third case](../master/pictures/ant-1-3.png)

![First hist](../master/pictures/ant-2-1.png)

![Second hist](../master/pictures/ant-2-2.png)
