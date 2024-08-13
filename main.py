import shutil, time, os, traceback, datetime, json, smtplib
from email.mime.text import MIMEText
from email.header import Header

with open('conf.json', 'r') as outfile:
    data = json.load(outfile)

moveFrom = data["moveFrom"]
moveTo = data["moveTo"]
current_time = time.time()
home = os.getcwd()

def free_space(move):
    free_space = round(shutil.disk_usage(move).free / 1073741824, 2)
    return free_space
def backup(move):
    os.chdir(os.path.join(os.getcwd(), move))
    list_of_files = os.listdir(move)
    for file in list_of_files:
        file_location = os.path.join(os.getcwd(), file)
        modification_time = os.path.getmtime(file_location)
        if (current_time - modification_time) <= 24 * 60 * 60:
            shutil.copy(os.path.join(move, file), moveTo)
def clear(move, name):
    fs = free_space(move)
    os.chdir(os.path.join(os.getcwd(), move))
    if fs < 20:
        needtoclear = ((20-fs)+2)*1024**3
        files = sorted((f for f in os.scandir(move) if f.is_file()), key=lambda x: x.stat().st_mtime)
        # Loop over files and delete until total size is less than limit.
        for f in files:
            if needtoclear > 0:
                mt = os.path.getmtime(f)
                if mt > 24*60*60*15:
                    needtoclear -= os.stat(f).st_size
                    os.remove(f)
                else:
                    break
            else:
                success(f'Очистка на {name} выполнена успешно!')
                break
    else:
        success(f'Свободного места на {name} достаточно, очистка не требуется')
def storageClear(): # Функция очистки файлов в хранилище
    os.chdir(os.path.join(os.getcwd(), moveTo))
    clear(moveTo, 'хранилище')

def success(message):
    os.chdir(os.path.join(os.getcwd(), home))
    with open('logs.log', 'a') as s:
        s.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n" + message + 2*'\n' )
def mail():
    login = "test23@titan-group.ru"
    password = "testtest23"
    recipients_emails = "it@titan-group.ru"

    msg = MIMEText('Произошел сбой в системе очистки дискового пространства записей видеонаблюдения, пожалуйста проверьте логи и исправьте ошибку', 'plain', 'utf-8')
    msg['Subject'] = Header('Сбой системы очистки диска', 'utf-8')
    msg['From'] = login
    msg['To'] = recipients_emails

    smtpObj = smtplib.SMTP('mail.titan-group.ru', 25)
    smtpObj.login(login, password)
    smtpObj.sendmail(msg['From'], recipients_emails, msg.as_string())
if __name__ == "__main__":
    try:
        success('Резервное копирование проведено успешно')
        for i in range(len(moveFrom)):
            backup(moveFrom[i])
            clear(moveFrom[i], 'диске')
        storageClear()
    except Exception:
        os.chdir(os.path.join(os.getcwd(), home))
        with open('logs.log', 'a') as f:
            f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n" + '{}\n'.format(traceback.format_exc()) + '\n')
            mail()
