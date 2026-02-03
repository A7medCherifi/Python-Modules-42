def preservation_system():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = 'new_discovery.txt'

    data = """New quantum algorithm discovered
Efficiency increased by 347%
Archived by Data Archivist trainee
"""

    print(f"Initializing new storage unit: {file_name}")
    try:
        with open(file_name, 'a') as f:
            print("Storage unit created successfully...\n")

            print("Inscribing preservation data...")
            for index, line in enumerate(data.splitlines(), start=1):
                txt = f"[ENTRY {index:03d}] {line}"
                f.write(txt + "\n")
                print(txt)
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{file_name}' ready for long-term preservation.")
    except Exception as e:
        print(f"ERROR: {e}")



if __name__ == "__main__":
    preservation_system()