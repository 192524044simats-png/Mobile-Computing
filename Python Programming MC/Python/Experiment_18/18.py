# Experiment 18: Call Blocking Probability using Erlang B
import math

def erlang_b(traffic, servers):
    blocking = 1.0
    for n in range(1, servers + 1):
        blocking = (traffic * blocking) / (n + traffic * blocking)
    return blocking

traffic_erlang = 10
channels = 14
blocking = erlang_b(traffic_erlang, channels)

print("EXPERIMENT 18 - ERLANG B CALL BLOCKING")
print(f"Offered traffic : {traffic_erlang} Erlangs")
print(f"Available lines : {channels}")
print(f"Blocking prob.  : {blocking:.5f}")
print(f"Blocking percent: {blocking * 100:.2f}%")


# Graph: Erlang B blocking probability versus number of channels
import matplotlib.pyplot as plt
channel_range = list(range(1, 26))
blocking_values = [erlang_b(traffic_erlang, c) * 100 for c in channel_range]
plt.figure(figsize=(8, 5))
plt.plot(channel_range, blocking_values, marker="o")
plt.title("Experiment 18: Erlang B Call Blocking")
plt.xlabel("Number of Channels")
plt.ylabel("Blocking Probability (%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("Graph_Screenshot.png", dpi=150)
plt.show()
