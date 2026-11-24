import math

# Experiment 16: Free-Space Path Loss and Received Power
frequency_mhz = 1800
distance_km = 2.0
tx_power_dbm = 30
tx_gain_dbi = 2
rx_gain_dbi = 2

fspl_db = 32.44 + 20 * math.log10(frequency_mhz) + 20 * math.log10(distance_km)
received_power_dbm = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - fspl_db

print("EXPERIMENT 16 - FREE-SPACE PATH LOSS")
print(f"Frequency       : {frequency_mhz} MHz")
print(f"Distance        : {distance_km} km")
print(f"Transmit Power  : {tx_power_dbm} dBm")
print(f"Free-space loss : {fspl_db:.2f} dB")
print(f"Received Power  : {received_power_dbm:.2f} dBm")


# Graph: Received power versus distance
import matplotlib.pyplot as plt
distances = [0.1, 0.2, 0.5, 1, 2, 3, 5, 8, 10]
powers = [tx_power_dbm + tx_gain_dbi + rx_gain_dbi -
          (32.44 + 20 * math.log10(frequency_mhz) + 20 * math.log10(d))
          for d in distances]
plt.figure(figsize=(8, 5))
plt.plot(distances, powers, marker="o")
plt.title("Experiment 16: Received Power vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Received Power (dBm)")
plt.grid(True)
plt.tight_layout()
plt.savefig("Graph_Screenshot.png", dpi=150)
plt.show()
