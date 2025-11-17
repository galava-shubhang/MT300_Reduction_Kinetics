'''
MT300: PIFA 
Reduction Kinetics
Python Programming Group Project

Team Members:
1. Anindith B. L. - 231MT008
2. Shubhang S. Galagali - 231MT049
3. Suhas Gowda M. - 231MT053
'''

import numpy as np
import matplotlib.pyplot as plt

# Normalized dimensionless time array initialized:
time = np.linspace(0, 1, 1000)

# Degree of reduction (F) as a function of time

# For spherical pellets:

# 1. Chemical Reaction Control (Shrinking Core Model)
# F = 1 - (1 - t)^3

F_chemical = 1 - (1 - time)**3

# 2. Diffusion Control through Product Layer (Shrinking Core Model)
# F = 1 - 3(1-t)^2 + 2(1-t)^3
F_diffusion = 1 - 3*(1 - time)**2 + 2*(1 - time)**3

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time, F_chemical, 'green', linewidth=2.5, label='Chemical Reaction Control')
plt.plot(time, F_diffusion, 'purple', linewidth=2.5, label='Diffusion Control')

# Formatting
plt.xlabel('Normalized Time (t/τ)', fontsize=12, fontweight='bold')
plt.ylabel('Degree of Reduction (F)', fontsize=12, fontweight='bold')
plt.title('Reduction Kinetics of Spherical Pellet:\nChemical vs Diffusion Control', 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='lower right')
plt.grid(True, alpha=0.3, linestyle='--')
plt.xlim(0, 1)
plt.ylim(0, 1)

# Add annotations to highlight differences
plt.annotate('Faster initial rate', xy=(0.3, 0.7), xytext=(0.15, 0.85),
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
            fontsize=10, color='green')
plt.annotate('Slower initial rate,\nlinear region', xy=(0.5, 0.5), xytext=(0.65, 0.3),
            arrowprops=dict(arrowstyle='->', color='purple', lw=1.5),
            fontsize=10, color='purple')

plt.tight_layout()
plt.show()

# Print key characteristics
print("=" * 60)
print("REDUCTION KINETICS COMPARISON")
print("=" * 60)
print("\nChemical Reaction Control:")
print("  - Faster initial reduction rate")
print("  - Follows: F = 1 - (1 - t/τ)³")
print("  - Rate limited by surface reaction")
print("\nDiffusion Control:")
print("  - Slower initial rate, but more linear")
print("  - Follows: F = 1 - 3(1 - t/τ)² + 2(1 - t/τ)³")
print("  - Rate limited by diffusion through product layer")
print("\nAt t/τ = 0.5:")
print(f"  Chemical Control: F = {F_chemical[500]:.3f}")
print(f"  Diffusion Control: F = {F_diffusion[500]:.3f}")
print("=" * 60)