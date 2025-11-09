# Job Sequencing with Deadlines - Simplest Greedy Code


n = int(input("Enter number of jobs: "))
jobs = []

print("\nEnter Job ID, Deadline, and Profit:")
for i in range(n):
    job_id, deadline, profit = input(f"Job {i+1}: ").split()
    jobs.append((job_id, int(deadline), int(profit)))

jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)
slots = [None] * (max_deadline + 1)
total_profit = 0


for job in jobs:
    job_id, deadline, profit = job
    for t in range(deadline, 0, -1):  
        if slots[t] is None:
            slots[t] = job_id
            total_profit += profit
            break


print("\nJob order for maximum profit:")
for i in range(1, max_deadline + 1):
    if slots[i]:
        print(f"Slot {i}: Job {slots[i]}")

print("\nTotal Profit:", total_profit)
