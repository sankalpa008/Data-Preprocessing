from statistics import mean, stdev

def smooth_by_bins(data, bin_size=3):
    result = []
    current_bin = []
    
    print("Original data:", data)
    print("\nSmoothing by bins (size=3):")
    
    for value in data:
        current_bin.append(value)
        if len(current_bin) == bin_size:
            bin_mean = round(mean(current_bin), 2)
            print(f"Bin {current_bin} → {bin_mean}")
            result.extend([bin_mean] * len(current_bin))
            current_bin = []
    
    if current_bin:
        bin_mean = round(mean(current_bin), 2)
        print(f"Bin {current_bin} → {bin_mean}")
        result.extend([bin_mean] * len(current_bin))
    
    print("\nSmoothed data:", result)
    
    data_mean = mean(data)
    data_std = stdev(data)
    outliers = [x for x in data if abs(x - data_mean) > 2 * data_std]
    print("\nOutliers (beyond 2 standard deviations):", outliers)

ages = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 
        30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
smooth_by_bins(ages)
