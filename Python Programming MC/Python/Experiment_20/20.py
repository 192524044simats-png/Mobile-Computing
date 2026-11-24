# Experiment 20: CDMA Spreading and Despreading
data_bits = [1, 0, 1, 1]
code = [1, 1, 1, -1]  # chip sequence (+1/-1)
chips = []

for bit in data_bits:
    bipolar = 1 if bit == 1 else -1
    chips.extend([bipolar * c for c in code])

# Despread each group by correlating with the spreading code
recovered = []
for start in range(0, len(chips), len(code)):
    group = chips[start:start + len(code)]
    correlation = sum(x * c for x, c in zip(group, code))
    recovered.append(1 if correlation > 0 else 0)

print("EXPERIMENT 20 - CDMA SPREADING / DESPREADING")
print("Original bits :", data_bits)
print("Spreading code:", code)
print("Transmitted chips:")
print(chips)
print("Despread bits :", recovered)
print("Successful    :", data_bits == recovered)


# Graph: Original data and spread chips
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(8, 6))
axes[0].step(range(len(data_bits)), data_bits, where="mid", marker="o")
axes[0].set_title("Original Data Bits")
axes[0].set_xlabel("Bit Index")
axes[0].set_ylabel("Bit")
axes[0].set_ylim(-0.2, 1.2)
axes[0].grid(True)
axes[1].stem(range(len(chips)), chips)
axes[1].set_title("CDMA Spread Chip Sequence")
axes[1].set_xlabel("Chip Index")
axes[1].set_ylabel("Chip Value")
axes[1].grid(True)
plt.tight_layout()
plt.savefig("Graph_Screenshot.png", dpi=150)
plt.show()
