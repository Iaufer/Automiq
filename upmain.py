from ftplib import FTP, error_perm
import argparse, os, shutil

ftp_host = '10.10.20.8'
ftp_user = 'user'
ftp_password = 'user'
locale_folders = "../tmp/test-230531/"

files = [
    {"name": "file1.txt", "endpoints": ["ftp", "folder"]},
    {"name": "file2.txt", "endpoints": ["owncloud", "ftp"]},
    {"name": "file3.txt", "endpoints": ["folder", "owncloud", "ftp"]}
]



def ArgumentParser():
    parser = argparse.ArgumentParser(description="Parsing args")
    
    parser.add_argument("-d", "--dry", action='store_true', help='Dry mode')
    parser.add_argument("-o", "--override", action='store_true', help='Overwrite file')
    parser.add_argument("path", help="Path to source files")

    args = parser.parse_args()

    return args



def copy_files_ftp(ftp, args_path, name_file):
    with open(args_path + '/' + name_file, 'rb') as local_file:
        ftp.storbinary(f'STOR {name_file}', local_file)
        
def copy_files_folder(where_to_copy, args_path, name_file):
    if not os.path.exists(where_to_copy):
        os.makedirs(where_to_copy)
        print(f'Папки {where_to_copy} созданы.')
    else:
        print(f'Папки {where_to_copy} уже созданы.')
        
    shutil.copy(args_path + '/' + name_file, where_to_copy)

def main():
    args = ArgumentParser()
    
    # if args.override:
    # print("Перезапись файлов будет произведена.")
        
    try:
        print("Попытка подключения...")
        ftp = FTP(ftp_host)
        
        print("Подключено к серверу.")
        
        print("Попытка входа...")
        ftp.login(ftp_user, ftp_password)
        print("Вход выполнен успешно!")
        
        
        
        for item in files:
            name_file = item['name']
            endpoints = item['endpoints']
            
            for end in endpoints:
                if end == "ftp":
                    if args.dry:
                        print(f'В режиме "сухого" запуска. Скопировать файл {name_file} на FTP.')
                    else:
                        copy_files_ftp(ftp, args.path, name_file)
                        
                if end == "folder":
                    if args.dry:
                        print(f'В режиме "сухого" запуска. Скопировать файл {name_file} в папку "tmp/test-230531".')
                    else:
                        copy_files_folder(locale_folders, args.path, name_file)

    except error_perm as e:
        print(f"Ошибка входа: {e}")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    # else:
    #     print("Перезапись файлов не производится.")



if __name__ == "__main__":
    main()