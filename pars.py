
#ПАРСЕР АГМУНТОВ ИЗ КОМАНДНОЙ СТРОКИ
import argparse, os

def main():
    parser = argparse.ArgumentParser(description="Parsing args")
    
    parser.add_argument("-o", "--override", action='store_true', help='Overwrite file')
    parser.add_argument("path", help="Path to source files")

    args = parser.parse_args()

    if args.override:
        print("Перезапись файлов будет произведена.")
    else:
        print("Перезапись файлов не производится.")


    print("Путь к файлам", args.path)


    folders = os.listdir(args.path)
    for item in folders:
        print(item)

if __name__ == "__main__":
    main()
