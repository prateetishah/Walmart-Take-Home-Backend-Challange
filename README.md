# Seat Allocation System

Problem Statement: To implement a seat allocation system with maximized customer satisfaction and customer safety.

Assumptions:

The theater has maximum 10 rows and 20 seats in each row.
For customer safety, there will be a buffer of 3 seats and/or one row.

	Input Assumptions:
	
	Input requests should be added in .txt file and format should be R### #.
	Requested seats should be at least 1 and at most 200.
	Requested seats should be less than or same as available seats.
	To check available seats, request format should be R### A.

	Output Assumptions:

	Output file will be a .txt file and will have a reservation identifier with allocated seats or the error message.

Customer Satisfaction and Customer safety:

For the best viewing experience, it will start allocation from the middle row.
For customer satisfaction, requested seats are grouped.
There will be a buffer of 3 seats after each reservation or total available seats, whichever is minimum.
If requested seats are less than or same as 20, the row will be filled first.
