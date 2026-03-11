import sys
import timeit

import importlib.util

def time_python_file(filepath):
    # Load the module from file
    spec = importlib.util.spec_from_file_location("module", filepath)
    module = importlib.util.module_from_spec(spec)
    
    # Time the execution
    start_time = timeit.default_timer()
    spec.loader.exec_module(module)
    end_time = timeit.default_timer()
    
    elapsed = end_time - start_time
    return f"Execution time: {elapsed:.6f} seconds\n"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python timer.py <day #>")
        sys.exit(1)
    
    day = sys.argv[1]
    p1 = time_python_file(f"{day}/part1.py")
    p2 = time_python_file(f"{day}/part22.py")

    print(p1, p2)