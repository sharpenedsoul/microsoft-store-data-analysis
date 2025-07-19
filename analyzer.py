import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
def load_data(filepath='data/msft.csv'):
    try:
        df = pd.read_csv(filepath)
        print("✅ Data loaded successfully.")
        return df
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        return None

# Display first 5 rows
def display_head(df):
    print("\n🔹 First 5 rows:")
    print(df.head())

# Display last 5 rows
def display_tail(df):
    print("\n🔹 Last 5 rows:")
    print(df.tail())

# Display all columns
def display_columns(df):
    print("\n🔹 CSV Columns:")
    for col in df.columns:
        print(f"- {col}")

# Show selected fields
def display_basic_info(df):
    print("\n🔹 Name, Category & Price:")
    print(df[['Name', 'Category', 'Price']])

# Summary stats
def display_stats(df):
    print("\n🔹 Statistical Summary:")
    print(df.describe())

# Apps with rating > 4.5
def display_top_rated(df):
    print("\n🔹 Applications with Rating > 4.5:")
    top_apps = df[df['Rating'] > 4.5][['Name', 'Rating']]
    print(top_apps.to_string(index=False))

# Line graphs for numerical stats
def plot_line_graphs(df):
    stats = df.describe()
    for idx in stats.index:
        plt.figure()
        plt.title(f'📈 Line Graph: {idx}')
        plt.xlabel('Columns')
        plt.ylabel(idx)
        plt.plot(stats.columns, stats.loc[idx])
        plt.tight_layout()
        plt.show()

# Bar graphs for numerical stats
def plot_bar_graphs(df):
    stats = df.describe()
    for idx in stats.index:
        plt.figure()
        plt.title(f'📊 Bar Graph: {idx}')
        plt.xlabel('Columns')
        plt.ylabel(idx)
        plt.bar(stats.columns, stats.loc[idx])
        plt.tight_layout()
        plt.show()

# Main menu function
def main():
    df = load_data()
    if df is None:
        return

    while True:
        print("\n🧠 Microsoft Store Data Analysis Menu")
        print("1. Display first 5 rows")
        print("2. Display last 5 rows")
        print("3. Show all column names")
        print("4. Display Name, Category & Price")
        print("5. Statistical Summary")
        print("6. Show apps with rating > 4.5")
        print("7. Line Graphs")
        print("8. Bar Graphs")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice (1–9): "))
        except ValueError:
            print("❌ Invalid input. Enter a number.")
            continue

        if choice == 1:
            display_head(df)
        elif choice == 2:
            display_tail(df)
        elif choice == 3:
            display_columns(df)
        elif choice == 4:
            display_basic_info(df)
        elif choice == 5:
            display_stats(df)
        elif choice == 6:
            display_top_rated(df)
        elif choice == 7:
            plot_line_graphs(df)
        elif choice == 8:
            plot_bar_graphs(df)
        elif choice == 9:
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid option. Please try again.")

# Entry point
if __name__ == "__main__":
    main()