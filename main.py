# Python program to calculate the average score
# of the last 10 matches of the Indian Hockey Team

# Sample data: Goals scored by India in last 10 matches
last_10_scores = [3, 2, 4, 1, 5, 3, 2, 4, 3, 2]

# Calculate average
average_score = sum(last_10_scores) / len(last_10_scores)

# Display results
print("Last 10 Match Scores:", last_10_scores)
print("Average Goals Scored in Last 10 Matches:", round(average_score, 2))
