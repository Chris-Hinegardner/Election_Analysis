
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
          

# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name


print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

County_Option = []
County_Votes = {}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the county name from each row.
        county_name = row[1]

        if county_name not in County_Option:

           # Add the county name to the candidate list.
            County_Option.append(county_name)

           # Begin tracking that county vote count.
            County_Votes[county_name] = 0

        # Add a vote to that county's count
        County_Votes[county_name] += 1

# 2: Track the largest county and county voter turnout.
for county_name in County_Votes:

    # Retrieve vote count of a candidate.
    votes =County_Votes[county_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = county_name

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    for candidate_name in candidate_votes:

      # Retrieve vote count and percentage
      votes = candidate_votes.get(candidate_name)
      vote_percentage = float(votes) / float(total_votes) * 100
      candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate's voter count and percentage to the
    # terminal.
      print(candidate_results)
        #  Save the candidate results to our text file.
      with open(file_to_save, "w") as txt_file:
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
      if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    with open(file_to_save, "w") as txt_file:
      txt_file.write(winning_candidate_summary)
