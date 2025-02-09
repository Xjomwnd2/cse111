import pandas as pd
import matplotlib.pyplot as plt
import pytest

def load_data(filename):
    """Load data from a CSV file.
    
    Parameters:
        filename: str - Path to the CSV file
    Returns:
        pandas.DataFrame - Loaded data
    """
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def create_line_plot(data, x_col, y_col, title):
    """Create a line plot from data.
    
    Parameters:
        data: pandas.DataFrame - Data to plot
        x_col: str - Column name for x-axis
        y_col: str - Column name for y-axis
        title: str - Plot title
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

def create_bar_plot(data, x_col, y_col, title):
    """Create a bar plot from data.
    
    Parameters:
        data: pandas.DataFrame - Data to plot
        x_col: str - Column name for x-axis
        y_col: str - Column name for y-axis
        title: str - Plot title
    """
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar', x=x_col, y=y_col)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def calculate_statistics(data, column):
    """Calculate basic statistics for a column.
    
    Parameters:
        data: pandas.DataFrame - Input data
        column: str - Column name to analyze
    Returns:
        dict - Dictionary containing statistics
    """
    stats = {
        'mean': data[column].mean(),
        'median': data[column].median(),
        'std': data[column].std(),
        'min': data[column].min(),
        'max': data[column].max()
    }
    return stats

def main():
    filename = input("Enter the path to your CSV file: ")
    data = load_data(filename)
    
    if data is not None:
        print("\nAvailable columns:", data.columns.tolist())
        x_col = input("Enter x-axis column name: ")
        y_col = input("Enter y-axis column name: ")
        
        plot_type = input("Enter plot type (line/bar): ").lower()
        title = input("Enter plot title: ")
        
        if plot_type == 'line':
            create_line_plot(data, x_col, y_col, title)
        elif plot_type == 'bar':
            create_bar_plot(data, x_col, y_col, title)
        
        print("\nStatistics for", y_col)
        stats = calculate_statistics(data, y_col)
        for stat, value in stats.items():
            print(f"{stat}: {value:.2f}")

# Test functions
def test_calculate_statistics():
    data = pd.DataFrame({
        'values': [1, 2, 3, 4, 5]
    })
    stats = calculate_statistics(data, 'values')
    assert stats['mean'] == 3
    assert stats['median'] == 3
    assert stats['min'] == 1
    assert stats['max'] == 5

if __name__ == "__main__":
    main()


