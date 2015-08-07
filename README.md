# OO-ModuleProject
As part of our Object Orientated Software Development module in Semester 1, we were given a project. This repository contains the code I wrote for the project, as well as the csv files were supplied with by our lecturer.

**Description of project (Taken from handout)**
The sales manager for your company wants a program that will
streamline the sales teams travel plans. He describes the problem to
you as follows:
Each month, a salesperson needs to leave their home city and visit
prospective customers in 4 other cities. These cities could be different
each month. The sales manager wants to minimise the travel costs by
choosing the most economic route between the cities for each sales
person.
*Rules* 	
• The first airport is the home airport and the other 4 are
destinations.
• Start and finish in first city. Visit each other city (at least) once
• There must be 5 days between trips so 7 trips in total can be
done in one month
• Distance between airports calculated as great circle flight
• Cost of leg calculated in local currency of city.
• The cost for a given leg of a journey is calculated as the
exchange rate of origin city airport versus the destination city
airport) multiplied by the distance
• The best route is the cheapest option
*Tasks*
• Create a program that will allow a user to choose 5 airports.
• The program needs to read a file with a list of sales people and
airports and write a file with the best routes calculated per sales
person
• A graphic user interface to allow a sales person to input their
routes and display the cost
*Data*
You will be provided with comma separates text files (csv files)
containing a list of airports, a list of currencies and a list of exchange
rates.

**Instructions for use**
To run the program you should run the projectMain.py file. This gives the user the option to select an employee from the list (generated from the csv file employees.csv) or to select their own airports. The program then calculates the cheapest route in accordance with the rules laid out above. 
We were also required to create tests which can be ran from the projectTest.py file (must be ran in an IDE).