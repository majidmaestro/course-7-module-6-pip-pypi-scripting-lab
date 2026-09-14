from datetime import datetime
import os

def generate_log(log_data, directory=None):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    if directory:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
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