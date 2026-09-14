from datetime import datetime
import os

def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    content = "\n".join(str(item) for item in log_data)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
