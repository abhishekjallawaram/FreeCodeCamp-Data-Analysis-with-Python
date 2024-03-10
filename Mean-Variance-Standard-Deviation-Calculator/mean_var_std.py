import numpy as np

def calculate(list_input):
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list to a 3 x 3 Numpy array
    matrix = np.array(list_input).reshape(3, 3)
    
    # Dictionary to store the results
    results = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    
    return results

# Example usage
if __name__ == "__main__":
    example_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    try:
        example_output = calculate(example_input)
        print(example_output)
    except ValueError as e:
        print(e)
