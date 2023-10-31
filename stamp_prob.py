# Function to count distinct country stamps
def count_distinct_stamps(N, stamps):
    # Create an empty set to store distinct country stamps
    distinct_stamps = set()
    
    # Iterate through the list of stamps and add them to the set
    for stamp in stamps:
        distinct_stamps.add(stamp)
    
    # Return the size of the set, which is the count of distinct country stamps
    return len(distinct_stamps)

# Read the input
N = int(input("Enter the total number of country stamps: "))
stamps = []
for _ in range(N):
    stamp = input()
    stamps.append(stamp)

# Call the function to count distinct stamps and print the result
distinct_count = count_distinct_stamps(N, stamps)
print("Total number of distinct country stamps:", distinct_count)
