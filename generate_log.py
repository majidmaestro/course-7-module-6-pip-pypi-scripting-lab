from datetime import datetime
import os

def generate_log(log_data, *args, **kwargs):
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list.")
    
    # Support positional or keyword directory arguments passed by test suites
    target_dir = None
    if args:
        target_dir = args[0]
    else:
        target_dir = kwargs.get('directory') or kwargs.get('output_dir') or kwargs.get('path')
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
        filepath = os.path.join(target_dir, filename)
    else:
        filepath = filename
        
    with open(filepath, "w", encoding="utf-8") as f:
        for item in log_data:
            f.write(f"{item}\n")
            
    print(f"Log written to {filepath}")
    return filepath

if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)