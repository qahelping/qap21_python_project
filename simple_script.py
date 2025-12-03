import os
from datetime import datetime
from pathlib import Path


def main():
    now = datetime.now().strftime("%d.%m.%Y")

    print("------> Docker start")
    print("------> Current date:", now)
    print("------> HELLO from container")

    app_name = os.getenv("APP_NAME", None)
    log_level = os.getenv("LOG_LEVEL", "INFO")

    if app_name:
        print(f"------> Docker start for {app_name}")

    if log_level == "INFO":
        print(f"------> {datetime.now()} - root - INFO - ")
    elif log_level == "CRITICAL":
        print(f"------> {datetime.now()}- root - CRITICAL - ")
    else:
        print("------> NONE")

    folder = Path("test_api")
    if folder.exists():
        print("------> FOLDER test_api EXISTS")

    data_dir = Path("/data")
    data_dir.mkdir(parents=True, exist_ok=True)
    out_file = data_dir / "output.txt"
    out_file.write_text("------> FOLDER test_api EXISTS")

    print("------> Finished")


main()
