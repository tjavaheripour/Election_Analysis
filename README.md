# Election_Analysis
python Programming  language
## Project Overview
A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6. 64bit, Visual Studio Code, 1.54.3

## Results
The analyses of the election show that

- There were 369,711 votes cast in the election.

- The candidates were:

    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The cadidates results were:

  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

- The winner of the election was:

  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

- The counties were:

  - Jefferson
  - Denver
  - Arapahoe

- The county results were:

  - Jefferson received 10.5% of the total votes with 38,855 votes.
  - Denver received 82.8% of the total votes with 306,055 votes.
  - Arapahoe received 6.7% of the total votes with 24,801 votes.

- The county with the highest turnout was:
  - Denver, which received 82.8% of the total votes and 306,055 number of votes.

Here, you can see the results of election_audit after running the code:

![election results.png](https://github.com/tjavaheripour/Election_Analysis/blob/main/election%20results.PNG)

## Summary
The script can be easily modified and used for any other election:

-	This script pulls data from the election_data.csv file, you can change the source of .csv file on the code by use of “ file_to_load” variable to be assigned with a different file for a specific election data.Also, you can use file_to_save variable to create a file to keep the result of this particular election . As you can see in the screenshot below:

        # Add a variable to load a file from a path.
        file_to_load = os.path.join("Resources", "election_results.csv")
        # Add a variable to save the file to a path.
        file_to_save = os.path.join("analysis", "election_analysis.txt")

-  The row function returns the values from a row with a particular index, for example  ‘candidate_name = row[2]’ shows that the third column of worksheet related to names of candidates, if we decide to run this election audit from another csv file with different structure or maybe new coulmns, we should make sure that the address of variable name match correctly with the column on the csv file to dreive data.
As shown below, currently we assign the “candidate_name” and “county_name” variables with their location in the row:

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
-  If you want capture more data from the voters in .csv file, such as count of  gender, age group ,etc. you could expand the list of variables like previous code and modify the current loop script by adding more if statement inside it 

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.

            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0


        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1
