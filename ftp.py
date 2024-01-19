from ftplib import FTP, error_perm

ftp_host = '192.168.169.135'
ftp_user = 'artyom'
ftp_password = '2505'
ftp_folder = 'SOSIKI'


try:
    print("Попытка подключения...")
    ftp = FTP(ftp_host)
    
    print("Подключено к серверу.")
    
    print("Попытка входа...")
    ftp.login(ftp_user, ftp_password)
    print("Вход выполнен успешно!")
    # ftp.mkd(ftp_folder)
    # print(f"Папка '{ftp_folder}' создана успешно.")
    ftp.rename(ftp_folder, 'KUSOK')
    ftp.dir()

    ftp.quit()

except error_perm as e:
    print(f"Ошибка входа: {e}")
except Exception as e:
    print(f"Ошибка подключения: {e}")
