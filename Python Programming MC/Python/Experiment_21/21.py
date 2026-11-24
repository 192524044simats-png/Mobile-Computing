# Experiment 21: OFDMA Downlink Scheduler - Throughput and Fairness
users = 4
resource_blocks = 12
# Each row is the achievable data rate (Mbps) for each user on an RB.
rates = [
    [8, 7, 6, 5],
    [9, 6, 7, 4],
    [7, 8, 5, 6],
    [10, 5, 6, 3],
    [8, 7, 8, 4],
    [9, 6, 7, 5],
    [6, 9, 5, 7],
    [8, 7, 6, 6],
    [10, 5, 7, 4],
    [7, 8, 6, 5],
    [9, 6, 8, 4],
    [8, 7, 5, 7],
]

def jain_index(values):
    total = sum(values)
    return total * total / (len(values) * sum(v * v for v in values))

# Max-rate scheduler: assign each RB to user with highest instantaneous rate.
max_rate = [0] * users
for rb in rates:
    winner = max(range(users), key=lambda u: rb[u])
    max_rate[winner] += rb[winner]

# Round-robin scheduler: give RBs cyclically, use that user's rate.
round_robin = [0] * users
for idx, rb in enumerate(rates):
    user = idx % users
    round_robin[user] += rb[user]

print("EXPERIMENT 21 - OFDMA SCHEDULER COMPARISON")
print(f"Resource blocks: {resource_blocks}")
print("\nScheduler       User throughput (Mbps)       Total      Jain fairness")
for name, result in [("Max-rate", max_rate), ("Round-robin", round_robin)]:
    print(f"{name:<14} {str(result):<28} {sum(result):>6.1f} Mbps   {jain_index(result):.3f}")
print("\nHigher Jain index (maximum 1.0) means more equal user throughput.")


# Graph: User throughput comparison for scheduling algorithms
import matplotlib.pyplot as plt
positions = list(range(users))
width = 0.35
plt.figure(figsize=(8, 5))
plt.bar([p - width/2 for p in positions], max_rate, width, label="Max-rate")
plt.bar([p + width/2 for p in positions], round_robin, width, label="Round-robin")
plt.title("Experiment 21: OFDMA User Throughput")
plt.xlabel("User")
plt.ylabel("Throughput (Mbps)")
plt.xticks(positions, [f"User {p+1}" for p in positions])
plt.grid(axis="y")
plt.legend()
plt.tight_layout()
plt.savefig("Graph_Screenshot.png", dpi=150)
plt.show()
