import random
import matplotlib.pyplot as plt

N = 10_000
TARGET = 30

results = []
for _ in range(N):
    base    = random.uniform(10, 20)
    traffic = random.uniform(0, 15)
    stop    = random.uniform(0, 8)
    results.append(base + traffic + stop)

on_time = sum(1 for t in results if t <= TARGET)
prob = on_time / N * 100
mean = sum(results) / N

print(f"Mean arrival : {mean:.1f} min")
print(f"P(≤ {TARGET} min)  : {prob:.1f}%")
print(f"Verdict      : {'✓ On time' if prob >= 50 else '✗ Late'}")

fig, ax = plt.subplots()
ax.hist(results, bins=50, color="#378add", edgecolor="none")
ax.axvline(x=TARGET, color="black", linestyle="--", linewidth=1.8, label=f"Target {TARGET} min ({prob:.1f}% on time)")
ax.axvline(x=mean,   color="red",   linestyle=":",  linewidth=1.8, label=f"Mean {mean:.1f} min")
ax.set_xlabel("Arrival time (min)")
ax.set_ylabel("Count")
ax.set_title("Monte Carlo Arrival Time")
ax.legend(loc="upper left", fontsize=9)
plt.tight_layout()
plt.savefig("monte_carlo_arrival.png", dpi=150)
plt.show()