
def bin_data(data, num_bins=3):
    print("Original data:", data)
    
    sorted_data = sorted(data)
    bin_size = len(data) // num_bins
    print("\nEqual-frequency binning:")
    for i in range(0, len(sorted_data), bin_size):
        bin_data = sorted_data[i:i + bin_size]
        print(f"Bin: {bin_data}")
        print(f"Average: {sum(bin_data)/len(bin_data):.2f}")
    
    min_val = min(data)
    max_val = max(data)
    bin_width = (max_val - min_val) / num_bins
    
    print("\nEqual-width binning:")
    bins = [[] for _ in range(num_bins)]
    for value in data:
        bin_index = min(int((value - min_val) / bin_width), num_bins - 1)
        bins[bin_index].append(value)
    
    for i, bin_data in enumerate(bins):
        if bin_data:
            print(f"Bin {i+1}: {bin_data}")
            print(f"Average: {sum(bin_data)/len(bin_data):.2f}")
        else:
            print(f"Bin {i+1}: Empty")

sales_prices = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]
bin_data(sales_prices)
