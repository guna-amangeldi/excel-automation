import pandas as pd

def clean_data(path: str) -> pd.DataFrame:
    """
    Load an Excel file, remove empty rows and
    add a Total column with the row-wise sum.
    """
    # Load the Excel file into a DataFrame
    df = pd.read_excel(path)

    # Remove rows that are completely empty
    df = df.dropna(how = "all")

    # Add a 'Total' column that sums numeric columns in each row
    df["Total"] = df.select_dtypes(include = "number").sum(axis=1)

    return df

if __name__ == "__main__":
    # Name of the input file (must exist in the same folder)
    input_file = "input.xlsx"

    # Run the cleaning function
    cleaned_df = clean_data(input_file)

    # Save result as a new Excel file
    cleaned_df.to_excel("output.xlsx", index=False)

    print("Report generated successfully: output.xlsx")
