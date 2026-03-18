from utils.system_info import get_system_info
from utils.sha_hashing import generate_system_id
import json


def main():
    # Step 1: Collect system fingerprint
    system_info = get_system_info()

    # Step 2: Generate unique system ID (SHA-256)
    system_id = generate_system_id(system_info)

    # Step 3: Display results
    print("\n===== SYSTEM INFORMATION =====")
    print(json.dumps(system_info, indent=4))

    print("\n===== UNIQUE SYSTEM ID (SHA-256) =====")
    print(system_id)


if __name__ == "__main__":
    main()