# Experiment 19: Handoff Simulation with Hysteresis
# A handoff occurs when neighbor signal exceeds serving signal by H dB.
serving = [ -72, -75, -79, -82, -84, -80, -77, -83 ]
neighbor = [ -80, -78, -75, -73, -71, -74, -79, -76 ]
hysteresis_db = 3
current_cell = "Cell A"
handoffs = 0

print("EXPERIMENT 19 - HANDOFF WITH HYSTERESIS")
print("Step | Cell A (dBm) | Cell B (dBm) | Connected")
for step, (a, b) in enumerate(zip(serving, neighbor), 1):
    if current_cell == "Cell A" and b >= a + hysteresis_db:
        current_cell = "Cell B"
        handoffs += 1
    elif current_cell == "Cell B" and a >= b + hysteresis_db:
        current_cell = "Cell A"
        handoffs += 1
    print(f"{step:>4} | {a:>12} | {b:>12} | {current_cell}")
print(f"\nHysteresis margin: {hysteresis_db} dB")
print(f"Total handoffs   : {handoffs}")


# Graph: Signal levels and hysteresis decision
import matplotlib.pyplot as plt
steps = list(range(1, len(serving) + 1))
plt.figure(figsize=(8, 5))
plt.plot(steps, serving, marker="o", label="Serving Cell A")
plt.plot(steps, neighbor, marker="s", label="Neighbor Cell B")
plt.title("Experiment 19: Handoff Signal Strength")
plt.xlabel("Simulation Step")
plt.ylabel("Signal Strength (dBm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("Graph_Screenshot.png", dpi=150)
plt.show()
