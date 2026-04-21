import argparse
from system_info_checker import get_system_info
from exporter import export_to_pdf

def print_system_info(info):
    print("\n--- SYSTEM INFO ---")
    for key, value in info.items():
        print(f"{key}: {value}")

def main():
    parser = argparse.ArgumentParser(description="System Info Checker Tool")

    parser.add_argument("--export", choices=["pdf"], help="Export report")
    parser.add_argument("--filename", help="Custom file name")

    args = parser.parse_args()

    info = get_system_info()
    print_system_info(info)

    if args.export == "pdf":
        filename = args.filename if args.filename else "system_report.pdf"
        export_to_pdf(info, filename)

if __name__ == "__main__":
    main()