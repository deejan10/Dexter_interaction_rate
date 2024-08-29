import numpy as np
import matplotlib.pyplot as plt

# Constants
interaction_constant = 1e-30  # Arbitrary interaction constant (Joules)
donor_lifetime = 1e-9  # Donor lifetime (seconds)

# Donor-acceptor distance range
distances = np.linspace(1e-9, 10e-9, 100)  # Distance from 1nm to 10nm

# Concentrations
cs_pbp_cl3_concentration = 25e-6  # 25 micro molar (constant)
ag_nps_concentration = 15e-6  # AgNPs concentration (constant)
ag_nps_sizes = np.linspace(2e-9, 2e-9, 1)  # AgNPs sizes (2nm to 6nm)

# Calculate Dexter energy transfer rate
def calculate_dexter_transfer_rate(distance, donor_concentration, acceptor_concentration, acceptor_size):
    return (interaction_constant * donor_concentration * acceptor_concentration) * np.exp(-2 * distance / acceptor_size)

# Calculate Dexter transfer rate for increasing AgNP sizes
dexter_rates = []
for ag_nps_size in ag_nps_sizes:
    dexter_rate = calculate_dexter_transfer_rate(distances, cs_pbp_cl3_concentration, ag_nps_concentration, ag_nps_size)
    dexter_rates.append(dexter_rate)

# Plot Dexter transfer rate for different AgNP sizes
plt.figure(figsize=(10, 5))

for i, size in enumerate(ag_nps_sizes):
    plt.plot(distances * 1e9, dexter_rates[i], label=f'AgNP Size = {size * 1e9} nm')

plt.xlabel('Donor-Acceptor Distance (nm)')
plt.ylabel('Dexter Transfer Rate (1/s)')
plt.title('Dexter Transfer Rate vs Distance for Different AgNP Sizes')
#plt.legend()
plt.tight_layout()
plt.show()