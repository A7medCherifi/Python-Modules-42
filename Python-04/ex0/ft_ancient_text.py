def data_recovery_system():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = 'ancient_fragment.txt'
    print(f"Accessing Storage Vault: {file_name}")

    try:
        print("Connection established...\n")
        with open(file_name, 'r') as f:
            data = f.read()
            print("RECOVERED DATA:")
            print(data)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    data_recovery_system()
