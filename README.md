# Election_Analysis
<h1 align="center"><Election Analysis</h1>

##<p align="center"><

This analysis aims to ensure the quality of the data provided, provide readily available statistics, and determine the winner of the elction.

*Total votes: 739,422

*County Votes:

*Jefferson: 3.5% (38,855)

*Denver: 27.6% (306,055)

*Arapahoe: 2.2% (24,801)

*Largest County Percentage: Denver: 27.6% (306,055)

###Canditate Vote Breakdown

*Charles Casper Stockham: 15.4% (170,426)

*Diana DeGette: 49.2% (545,784)

*Raymon Anthony Doane: 2.1% (23,212)

###Winner Breakdown:

*Winner: Diana DeGette

*Winning Vote Count: 272,892

*Winning Percentage: 73.8%

This program is designed to be flexible. A few variable changes will pull these results for any election data. The "With" statement fuction and "for" loop functions are the crucial pieces of our program that allow this flexibility. I will explain those variables with example below.

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    <h1 style="color:blue;">This reads the header row to find our desired values.</h1>
    headers = next(file_reader)
    for row in file_reader:
         <h1 style="color:blue;">This adds our total vote count.</h1>
        total_votes += 1

         <h1 style="color:blue;">This prints all the candidate's names from each row.</h1>
        candidate_name = row[2]
        <h1 style="color:blue;">This ensures we get each candidates name only once.</h1>
        if candidate_name not in candidate_options:


            candidate_options.append(candidate_name)
        <h1 style="color:blue;">Finally, this is how we add votes to each candidate.</h1>
            Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

         Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

You Can see in this breakdown that by changing "Candidate_Name" to "County_Name" and searching the appropriate row of data we can achieve various desired matrics with limited modification of our initial code. This gives us the flexibility to efficiently find desired ellction metrics in the future.

></p>