import os
import json

def update_ids_in_json(directory):
    # Counter to assign incremental IDs across all files
    global_id = 1
    
    # Iterate through all JSON files in the directory
    for filename in sorted(os.listdir(directory)):
        print(filename)
        if filename.endswith(".jsonl"):
            file_path = os.path.join(directory, filename)
            print(file_path)

            updated_lines = []
            
            # Read the JSON file
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:

                    line = line.strip()
                    if not line:
                        continue
                    data = json.loads(line)
            
                    data["id"] = global_id
                    global_id += 1
                    print(global_id)

                    updated_lines.append(data)
            
            # Write all updated JSON data back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                for updated_line in updated_lines:
                    file.write(json.dumps(updated_line) + '\n')
    
    print("IDs updated successfully!")

# Example usage
directory = r"C:\Users\tomng\Desktop\Training_Data_Test"  # Replace with the path to your directory
update_ids_in_json(directory)
