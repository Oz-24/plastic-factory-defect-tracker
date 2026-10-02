import os
import numpy as np
import pandas as pd


def generate_production_data(filename="data/production_logs.csv"):
    """Simulates a 10-batch plastic manufacturing production ledger."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Fixed seed for identical data generation across runs
    np.random.seed(88)

    batches = [f"Batch_{i:03d}" for i in range(1, 11)]
    plastic_types = [
        "PET",
        "HDPE",
        "PET",
        "PP",
        "PP",
        "HDPE",
        "LDPE",
        "PET",
        "LDPE",
        "PP",
    ]

    # Generate total raw plastic material used per batch (in Kilograms, 500kg to 2000kg)
    total_mass_kg = np.random.randint(500, 2001, size=len(batches)).astype(
        float
    )

    # Generate scrap/waste plastic mass produced during molding (in Kilograms, 10kg to 150kg)
    scrap_mass_kg = np.random.randint(10, 151, size=len(batches)).astype(float)

    # Introduce missing data: 2 scrap logs were missed due to a weighing scale scale calibration error
    scrap_mass_kg[2] = np.nan
    scrap_mass_kg[6] = np.nan

    # Create the structural DataFrame grid
    df = pd.DataFrame(
        {
            "Batch_ID": batches,
            "Plastic_Polymer": plastic_types,
            "Total_Mass_Input_KG": total_mass_kg,
            "Scrap_Mass_Output_KG": scrap_mass_kg,
        }
    )

    df.to_csv(filename, index=False)
    print(f"Raw industrial manufacturing logs saved to: {filename}")


def analyze_factory_efficiency(filename="data/production_logs.csv"):
    """Cleans factory sensor data and computes structural matrix efficiency metrics."""
    # 1. Pandas: Load the manufacturing dataset
    df = pd.read_csv(filename)

    # 2. Pandas: Impute Missing Factory Data
    # If a scrap log is missing, fill it with the mean scrap weight of that specific plastic polymer
    mean_scrap = df["Scrap_Mass_Output_KG"].mean()
    df["Scrap_Mass_Output_KG"] = df["Scrap_Mass_Output_KG"].fillna(mean_scrap)

    # 3. NumPy: Vectorized Industrial Metric Extraction
    # Convert columns to underlying NumPy arrays for memory efficiency
    total_arr = df["Total_Mass_Input_KG"].to_numpy()
    scrap_arr = df["Scrap_Mass_Output_KG"].to_numpy()

    # Calculate Waste Percentage per batch using element-wise array division
    df["Waste_Percentage"] = np.round((scrap_arr / total_arr) * 100, 2)

    # 4. NumPy: Conditional Sustainability Threshold Masks
    # Exeter focuses heavily on sustainability; flag any batch with > 8% structural material waste
    waste_pct_arr = df["Waste_Percentage"].to_numpy()
    df["Sustainability_Status"] = np.where(
        waste_pct_arr > 8.0, "EXCESSIVE WASTE", "OPTIMAL"
    )

    # 5. Descriptive Factory Analytics via NumPy
    factory_stats = {
        "Total Raw Plastic Processed (KG)": np.sum(total_arr),
        "Total Material Wasted (KG)": np.sum(scrap_arr),
        "Average Manufacturing Waste Rate": np.mean(waste_pct_arr),
    }

    # 6. Pandas: Polymer Grouping Matrix Split
    polymer_summary = (
        df.groupby("Plastic_Polymer")["Waste_Percentage"].mean().to_dict()
    )

    return df, factory_stats, polymer_summary


if __name__ == "__main__":
    # Execute the industrial optimization pipeline
    generate_production_data()
    processed_df, general_stats, polymer_splits = analyze_factory_efficiency()

    print("\n--- PROCESSED PLASTIC MANUFACTURING REGISTRY ---")
    print(
        processed_df[
            [
                "Batch_ID",
                "Plastic_Polymer",
                "Total_Mass_Input_KG",
                "Scrap_Mass_Output_KG",
                "Waste_Percentage",
                "Sustainability_Status",
            ]
        ]
    )

    print("\n--- FACTORY-WIDE PERFORMANCE METRICS ---")
    for metric, score in general_stats.items():
        print(
            f"{metric}: {score:.2f} kg"
            if "Total" in metric
            else f"{metric}: {score:.2f}%"
        )

    print("\n--- AVERAGE WASTE RATE BY POLYMER TYPE ---")
    for polymer, avg_waste in polymer_splits.items():
        print(f"{polymer}: {avg_waste:.2f}%")
