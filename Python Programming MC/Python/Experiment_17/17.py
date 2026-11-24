import math

# Experiment 17: Frequency Reuse, Cluster Size, Capacity and S/I
i, j = 2, 1
channels_total = 420
sectors = 1
path_loss_exponent = 4

cluster_size = i * i + i * j + j * j
reuse_ratio = math.sqrt(3 * cluster_size)
channels_per_cell = channels_total // cluster_size
capacity = channels_per_cell * sectors
signal_interference = (reuse_ratio ** path_loss_exponent) / 6
si_db = 10 * math.log10(signal_interference)

print("EXPERIMENT 17 - FREQUENCY REUSE")
print(f"Reuse integers (i,j): ({i},{j})")
print(f"Cluster size N       : {cluster_size}")
print(f"Reuse ratio Q        : {reuse_ratio:.2f}")
print(f"Channels per cell    : {channels_per_cell}")
print(f"Capacity per cell    : {capacity} channels")
print(f"Approx. S/I          : {signal_interference:.2f}")
print(f"S/I in dB            : {si_db:.2f} dB")


# Graph: S/I and channel capacity for cluster sizes
import matplotlib.pyplot as plt
cluster_values = [1, 3, 4, 7, 9, 12, 13, 16, 19]
si_values = [10 * math.log10((math.sqrt(3 * n) ** path_loss_exponent) / 6)
             for n in cluster_values]
channel_values = [channels_total // n for n in cluster_values]
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(cluster_values, si_values, marker="o", label="Approx. S/I (dB)")
ax.set_xlabel("Cluster Size")
ax.set_ylabel("S/I (dB)")
ax.set_title("Experiment 17: S/I vs Cluster Size")
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("Graph_Screenshot.png", dpi=150)
plt.show()
