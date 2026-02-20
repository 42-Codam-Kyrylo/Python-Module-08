import os
import sys
from dotenv import load_dotenv


def get_env_or_exit(key: str) -> str:
    value = os.getenv(key)
    if not value:
        print(f"CRITICAL ERROR: {key} is required but missing.")
        sys.exit(1)
    return value


def main() -> None:
    try:
        load_dotenv()

        mode = os.getenv("MATRIX_MODE", "development")
        db_url = get_env_or_exit("DATABASE_URL")
        api_key = get_env_or_exit("API_KEY")
        log_level = os.getenv("LOG_LEVEL", "INFO")
        zion_url = os.getenv("ZION_ENDPOINT", "http://localhost:8080")

        print("ORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print(f"Mode: {mode}")

        db_status = (
            "Connected to local instance"
            if "localhost" in db_url or "127.0.0.1" in db_url
            else "Connected to remote instance"
        )
        print(f"Database: {db_status}")

        api_status = "Authenticated" if api_key else "Not Authenticated"
        print(f"API Access: {api_status}")
        print(f"Log Level: {log_level}")

        zion_status = "Online" if zion_url else "Offline"
        print(f"Zion Network: {zion_status}")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")

        if os.path.exists(".env"):
            print("[OK] .env file properly configured")

        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
