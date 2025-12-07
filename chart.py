"""
Customer Analytics: Purchase Amount Distribution by Customer Segment
Author: 24f2001048@ds.study.iitm.ac.in
Company: Christiansen Muller and Davis

This script generates a professional Seaborn boxplot visualization showing
the distribution of purchase amounts across different customer segments.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic customer purchase data
def generate_customer_data():
    """
    Generate synthetic purchase data for different customer segments.
    
    Returns:
        pd.DataFrame: Customer purchase data with segments and amounts
    """
    # Define customer segments with different spending characteristics
    segments = {
        'Premium': {'mean': 250, 'std': 60, 'n': 150},
        'Standard': {'mean': 150, 'std': 40, 'n': 200},
        'Basic': {'mean': 75, 'std': 25, 'n': 180},
        'Occasional': {'mean': 120, 'std': 80, 'n': 120}
    }
    
    # Generate data for each segment
    data = []
    for segment, params in segments.items():
        # Generate purchase amounts with realistic distribution
        amounts = np.random.gamma(
            shape=2, 
            scale=params['mean']/2, 
            size=params['n']
        )
        
        # Add some realistic noise and ensure positive values
        amounts = np.maximum(amounts + np.random.normal(0, params['std']/4, params['n']), 10)
        
        # Create records
        for amount in amounts:
            data.append({
                'Customer Segment': segment,
                'Purchase Amount ($)': round(amount, 2)
            })
    
    return pd.DataFrame(data)

# Generate the data
df = generate_customer_data()

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Set color palette - professional and colorblind-friendly
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
palette = sns.color_palette(colors)

# Create figure with exact dimensions for 512x512 output
# Use figsize that will result in exactly 512x512 pixels
fig, ax = plt.subplots(figsize=(512/80, 512/80), dpi=80)

# Create the boxplot
sns.boxplot(
    data=df,
    x='Customer Segment',
    y='Purchase Amount ($)',
    palette=palette,
    linewidth=2.5,
    flierprops={
        'marker': 'o',
        'markerfacecolor': 'gray',
        'markersize': 6,
        'linestyle': 'none',
        'markeredgecolor': 'darkgray',
        'alpha': 0.6
    },
    boxprops={'edgecolor': 'black', 'linewidth': 1.5},
    whiskerprops={'color': 'black', 'linewidth': 1.5},
    capprops={'color': 'black', 'linewidth': 1.5},
    medianprops={'color': 'darkred', 'linewidth': 2.5},
    ax=ax
)

# Customize the plot
ax.set_title(
    'Purchase Amount Distribution by Customer Segment',
    fontsize=14,
    fontweight='bold',
    pad=15
)

ax.set_xlabel(
    'Customer Segment',
    fontsize=12,
    fontweight='bold'
)

ax.set_ylabel(
    'Purchase Amount ($)',
    fontsize=12,
    fontweight='bold'
)

# Add grid for better readability
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='center')

# Add subtle background color
ax.set_facecolor('#F9F9F9')

# Save the chart with exact specifications: 512x512 pixels
# Remove bbox_inches='tight' to maintain exact dimensions
fig.savefig('chart.png', dpi=80, facecolor='white')

print("Chart generated successfully: chart.png (512x512 pixels)")
print(f"\nDataset Summary:")
print(f"Total customers analyzed: {len(df)}")
print(f"\nPurchase statistics by segment:")
print(df.groupby('Customer Segment')['Purchase Amount ($)'].describe().round(2))
