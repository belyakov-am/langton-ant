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

The square with size 3x3 was analyzed and ant was launched 2.5 * 10^5 times. 

## Notes to pictures below
0 - white colour, 1 - blue colour, 2 - lilac colour

