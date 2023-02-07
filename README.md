# Big-Data-MapReduce

Hi! This was a part of my Big Data Class where we tried to replicate the Map - Reduce process on Python.

Function: 	Description	Input of this function	Output of this function
Data cleaning function:	Some data cleaning jobs, such as removing punctuations and special symbols, converting string to integer (you need to do that to calculate the max.), etc.	Raw text data	Clean date, temperature pairs in proper data structure. 
Data split function:	Split the dataset into two parts:
Part1 includes the first 500 lines of the Raw data, Part2 includes the rest 500 lines
Output of data cleaning function:	Two separated subsets: Part1 and Part2. Save them as objects in Python
Mapper function: 	Two mapper functions that produce a set of key-value pairs for Part1 and Part2 subsets respectively. 	Output of data split function	Key-value pairs of Part1 and Part2.
Sort function:	Sort by key of Part1 and Part2 together, with an ascending sort order	Output of mapper function	Sorted Key-value pairs for the whole dataset
Partition function: 	All the months in year 2010 to 2015 are sent to Reducer1, and the others (2016 to 2020) are sent to Reducer2.	Output of sort function	Two ascending
ordered partitions.
Reducer function:	Collect all values belonging to the key and find the maximum temperature for the two ordered partitions.	Output of partition function	Maximum temperature of the ordered partitions. 
Main function:	Wrap all the steps together and combine the output of the two partitions together.	Output of reducer function	Final result of max temperature.
