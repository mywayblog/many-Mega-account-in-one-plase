# Импортируем необходимые библиотеки
import os
from mega import Mega
import threading

# Создаем объекты для работы с облачными хранилищами MEGA
# Замените email и password на свои учетные данные для каждого хранилища
mega1 = Mega()
mega2 = Mega()
mega3 = Mega()
m1 = mega1.login(email="jotridurta@gufum.com", password="Bze:MWzaqTC8!Qt")
m2 = mega2.login(email="hertojoknu@gufum.com", password="Wh5_qU8P-G}w}e)")
m3 = mega3.login(email="gortopugna@gufum.com", password="mMA=$3H)V.bEeJ9")

# Определяем путь к локальной папке, в которой будем синхронизировать файлы
# Замените folder на свой путь к папке
folder = "C:\\Users\\ПК\\MEGA"


def main_dowload(m,filename,folder):
    try:
        m.download(m.find(filename),folder) 
        # print('скачалось')
    except :
        print('скачалось')


# Создаем функцию для синхронизации одного облачного хранилища с локальной папкой
def sync(m, name):
    # Получаем список файлов в облачном хранилище
    files = m.get_files()
    # files_array = []
    # Перебираем все файлы в хранилище
    for file in files.values():
        # Проверяем, является ли файл обычным файлом, а не папкой
        if file["t"] == 0:
            # Получаем имя файла
            filename = file["a"]["n"]
            # files_array.append(filename)

            # Получаем путь к файлу в локальной папке
            filepath = os.path.join(folder, filename)
            # Проверяем, существует ли такой файл в локальной папке
            if os.path.exists(filepath):
                # Если существует, то сравниваем размеры файлов
                size_local = os.path.getsize(filepath)
                size_cloud = file["s"]
                # Если размеры разные, то считаем, что файл был изменен
                if size_local != size_cloud:
                    # Загружаем новую версию файла из облачного хранилища
                    print(f"Downloading {filename} from {name}...")
                    main_dowload(m,filename,folder)

            else:
                # Если не существует, то загружаем файл из облачного хранилища
                print(f"Downloading {filename} from {name}...")
                main_dowload(m,filename,folder)
    # Перебираем все файлы в локальной папке
    # for filename in os.listdir(folder):
    #     # Получаем путь к файлу в локальной папке
    #     filepath = os.path.join(folder, filename)
    #     # Проверяем, является ли файл обычным файлом, а не папкой
    #     if os.path.isfile(filepath):
    #         # Проверяем, существует ли такой файл в облачном хранилище
    #         if not m.find(filename):
    #             # Если не существует, то загружаем файл в облачное хранилище
    #             print(f"Uploading {filename} to {name}...")
    #             m.upload(filepath)

# Создаем функцию для запуска синхронизации в трех отдельных потоках
def run():
    # Создаем три потока для каждого облачного хранилища
    t1 = threading.Thread(target=sync, args=(m1, "MEGA1"))
    t2 = threading.Thread(target=sync, args=(m2, "MEGA2"))
    t3 = threading.Thread(target=sync, args=(m3, "MEGA3"))
    # Запускаем потоки
    t1.start()
    t2.start()
    t3.start()
    # Ждем, пока потоки завершатся
    t1.join()
    t2.join()
    t3.join()
    # Выводим сообщение о завершении синхронизации
    print("Sync completed")

# Запускаем функцию синхронизации
run()





























# # Импортируем необходимые библиотеки
# import os
# from mega import Mega
# import threading

# # Создаем объекты для работы с облачными хранилищами MEGA
# # Замените email и password на свои учетные данные для каждого хранилища
# mega1 = Mega()
# mega2 = Mega()
# mega3 = Mega()
# m1 = mega1.login(email="jotridurta@gufum.com", password="Bze:MWzaqTC8!Qt")
# m2 = mega2.login(email="hertojoknu@gufum.com", password="Wh5_qU8P-G}w}e)")
# m3 = mega3.login(email="gortopugna@gufum.com", password="mMA=$3H)V.bEeJ9")

# # Определяем путь к локальной папке, в которой будем синхронизировать файлы
# # Замените folder на свой путь к папке
# folder = "C:\\Users\\ПК\\MEGA\\Sublime Text Build 3211 x64"

# files_array = []
# files = m1.get_files()


# # Перебираем все файлы в хранилище
# for file in files.values():
#     # Проверяем, является ли файл обычным файлом, а не папкой
#     if file["t"] == 0:
#         # Получаем имя файла
#         filename = file["a"]["n"]
#         files_array.append(filename)


# for f in files_array:

#     fi = m1.find(f) 
#     # print(file)

    # try:
    #     m1.download(fi,folder) 
    #     print('скачалось')
    # except :
    #     print('ошибка но вроде скачалось')





# FIND FILE 
# file = m1.find('snapedit_1699199853926.png') 
# print(file)
# THEN DOWNLOAD USING THE FILE OBJECT 

# try:
#     m1.download(file) 
# except :
#     print('ошибка')

# Перебираем все файлы в хранилище
# for file in files.values():
#     # Проверяем, является ли файл обычным файлом, а не папкой
#     if file["t"] == 0:
#         # Получаем имя файла
#         filename = file["a"]["n"]
#         # Получаем путь к файлу в локальной папке
#         filepath = os.path.join(folder, filename)
#         # Проверяем, существует ли такой файл в локальной папке
#         if os.path.exists(filepath):
#             # Если существует, то сравниваем размеры файлов
#             size_local = os.path.getsize(filepath)
#             size_cloud = file["s"]
#             # Если размеры разные, то считаем, что файл был изменен
#             if size_local != size_cloud:
#                 # Проверяем, существует ли такой файл в облачном хранилище
#                 if m1.find(filename):
#                     # Если существует, то загружаем новую версию файла из облачного хранилища
#                     print(f"Downloading {filename} from MEGA1...")
#                     m1.download(file, filepath)
#                 else:
#                     # Если не существует, то выводим сообщение об ошибке
#                     print(f"File {filename} does not exist in MEGA1")
#         else:
#             # Если не существует, то проверяем, существует ли такой файл в облачном хранилище
#             if m1.find(filename):
#                 # Если существует, то загружаем файл из облачного хранилища
#                 print(f"Downloading {filename} from MEGA1...")
#                 m1.download(file, filepath)
#             else:
#                 # Если не существует, то выводим сообщение об ошибке
#                 print(f"File {filename} does not exist in MEGA1")


# THEN DOWNLOAD USING THE FILE OBJECT 

# SPECIFY DOWNLOAD LOCATION 
# m.download(file, '/home/john-smith/Desktop') 



# # Создаем функцию для синхронизации одного облачного хранилища с локальной папкой
# def sync(m, name):
#     # Получаем список файлов в облачном хранилище
#     files = m.get_files()
#     print(files)
#     # Перебираем все файлы в хранилище
    
#     on = ('QilWTCoL', {'h': 'QilWTCoL', 'p': 'pyV20TwS', 'u': 'nMs1Rs0Ev28', 't': 0, 'a': {'c': 'GKC_JbggzvaDGoWshIE5ywRtu0dl', 'n': 'snapedit_1699199853926.png'}, 'k': (1948100844, 1629967873, 2968662074, 157282304), 's': 278451, 'fa': '700:0*NsLyQ0dzt_k/700:1*lM3lks_DViY', 'ts': 1700302747, 'iv': (255723573, 303580911, 0, 0), 'meta_mac': (2638345450, 1735082049), 'key': (2065932505, 1933512942, 766756048, 1848946753, 255723573, 303580911, 2638345450, 1735082049)})



    # for file in files.values():
    #     # Проверяем, является ли файл обычным файлом, а не папкой
    #     if file["t"] == 0:
    #         # Получаем имя файла
    #         filename = file["a"]["n"]
    #         # print(filename)
    #         # Получаем путь к файлу в локальной папке
    #         filepath = os.path.join(folder, filename)
    #         # print(filepath)
    #         # Проверяем, существует ли такой файл в локальной папке
    #         if os.path.exists(filepath):
    #             # Если существует, то сравниваем размеры файлов
    #             size_local = os.path.getsize(filepath)
    #             size_cloud = file["s"]
    #             # Если размеры разные, то считаем, что файл был изменен
    #             if size_local != size_cloud:
    #                 # Загружаем новую версию файла из облачного хранилища
    #                 print(f"Downloading {filename} from {name}...")
    #                 m.download(file, filepath)
    #         else:
    #             # Если не существует, то загружаем файл из облачного хранилища
    #             print(f"Downloading {filename} from {name}...")
    #             m.download(file, filepath)
    # # Перебираем все файлы в локальной папке
    # for filename in os.listdir(folder):
    #     # Получаем путь к файлу в локальной папке
    #     filepath = os.path.join(folder, filename)
    #     # Проверяем, является ли файл обычным файлом, а не папкой
    #     if os.path.isfile(filepath):
    #         # Проверяем, существует ли такой файл в облачном хранилище
    #         if not m.find(filename):
    #             # Если не существует, то загружаем файл в облачное хранилище
    #             print(f"Uploading {filename} to {name}...")
    #             m.upload(filepath)

# Создаем функцию для запуска синхронизации в трех отдельных потоках
# def run():
#     # Создаем три потока для каждого облачного хранилища
    # t1 = threading.Thread(target=sync, args=(m1, "MEGA1"))
#     t2 = threading.Thread(target=sync, args=(m2, "MEGA2"))
#     t3 = threading.Thread(target=sync, args=(m3, "MEGA3"))
#     # Запускаем потоки
    # t1.start()
#     t2.start()
#     t3.start()
#     # Ждем, пока потоки завершатся
    # t1.join()
#     t2.join()
#     t3.join()
#     # Выводим сообщение о завершении синхронизации
    # print("Sync completed")

# # Запускаем функцию синхронизации
# run()