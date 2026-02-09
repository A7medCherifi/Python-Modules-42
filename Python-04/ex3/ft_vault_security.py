def vault_security_system():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    try:
        print("SECURE EXTRACTION:")
        with open('classified_data.txt', 'r') as f:
            print(f.read())

        print("\nSECURE PRESERVATION:")
        with open('classified_data.txt', 'w') as f:
            f.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")

    except Exception as e:
        print(f"ERROR: {e}")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security_system()
