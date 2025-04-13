from statistics import mean

def normalize_data(data):
    print("Original data:", data)
    
    min_val = min(data)
    max_val = max(data)
    min_max_norm = [(x - min_val) / (max_val - min_val) for x in data]
    print("\nMin-max normalization (0-1):")
    print([round(x, 2) for x in min_max_norm])
    
    data_mean = mean(data)
    std_dev = (sum((x - data_mean) ** 2 for x in data) / len(data)) ** 0.5
    z_score = [(x - data_mean) / std_dev for x in data]
    print("\nZ-score normalization:")
    print([round(x, 2) for x in z_score])
    
    max_abs = max(abs(x) for x in data)
    j = len(str(int(max_abs)))
    decimal_scaled = [x / (10 ** j) for x in data]
    print("\nDecimal scaling:")
    print([round(x, 4) for x in decimal_scaled])

numbers = [200, 300, 400, 600, 1000]
normalize_data(numbers)
