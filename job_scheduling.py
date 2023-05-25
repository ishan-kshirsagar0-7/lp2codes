profit = [15, 27, 10, 100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2, 3, 3, 3, 4]
profitNJobs = sorted(zip(profit, jobs, deadline), key=lambda x: x[0], reverse=True)
slot = [0] * len(jobs)
profit = 0
ans = ['null'] * len(jobs)

for i in range(len(jobs)):
    job = profitNJobs[i]
    for j in range(job[2], 0, -1):
        if slot[j] == 0:
            ans[j] = job[1]
            profit += job[0]
            slot[j] = 1
            break

print("Jobs scheduled:", ans[1:])
print(profit)