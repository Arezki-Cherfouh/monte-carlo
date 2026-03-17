# Monte Carlo Arrival Time Simulation

Simulates arrival time using 10,000 random trials across three variables, then plots the distribution and tells you the probability of arriving on time.

## Usage

```bash
pip install matplotlib
python main.py
```

## Variables

| Variable      | Range       |
| ------------- | ----------- |
| Base travel   | 10 – 20 min |
| Traffic delay | 0 – 15 min  |
| Stop duration | 0 – 8 min   |

Adjust the `uniform(min, max)` ranges and `TARGET` at the top of the script to match your scenario.

## Output

- Probability of arriving within the target time
- Mean arrival time
- Histogram plot with reference lines
