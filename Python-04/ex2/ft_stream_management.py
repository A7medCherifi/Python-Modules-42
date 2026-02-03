import sys


def communication_system():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    stats_report = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: {stats_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")

if __name__ == "__main__":
    communication_system()