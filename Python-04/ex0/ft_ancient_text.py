import sys


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
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    data_recovery_system()
