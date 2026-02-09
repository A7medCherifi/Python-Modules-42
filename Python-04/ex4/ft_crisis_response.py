def crisis_response_system(file_name: str):
    try:
        with open(file_name, 'r') as f:
            data = f.read()

            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            for i, line in enumerate(data.splitlines()):
                if line:
                    print(f"SUCCESS: Archive recovered - ``{line}''")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")


def test_crisis_system():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        crisis_response_system('lost_archive.txt')
        crisis_response_system('classified_vault.txt')
        crisis_response_system('standard_archive.txt')

        print("All crisis scenarios handled successfully. Archives secure.")
    except Exception as e:
        print(f"ERROR: {e}\n")


if __name__ == "__main__":
    test_crisis_system()
