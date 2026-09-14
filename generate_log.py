from datetime import datetime
import os

def generate_log(log_data, output_dir=None, directory=None):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")
    
    target_dir = output_dir or directory
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
        filepath = os.path.join(target_dir, filename)
    else:
        filepath = filename
        
    content = "\n".join(str(item) for item in log_data)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Log written to {filepath}")
    return filepath

if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
