def analyze_complexity(func_code):
    import time
    import ast

    # Calculate runtime
    start_time = time.time()
    exec(func_code)
    runtime = time.time() - start_time

    # Estimate Big O complexity
    complexity = "O(n)"  # Placeholder logic
    # This would require a more sophisticated analysis depending on the function's logic

    return runtime, complexity

if __name__ == '__main__':
    user_function = input("Enter function code: ")
    runtime, big_o = analyze_complexity(user_function)
    print(f'Estimated Runtime: {runtime} seconds')
    print(f'Estimated Big O Complexity: {big_o}')