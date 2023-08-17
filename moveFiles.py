import os
import shutil

while True:
    from_dir = ""
    to_dir = ""

    while True:
        from_dir = input("Diretório original: ")
        to_dir = input("Diretório de destino: ")

        boolA = os.path.exists(from_dir)
        boolB = os.path.exists(to_dir)

        if boolA and boolB:
            break
        else:
            print("Um dos caminhos de diretório é inválido, tente novamente")

    listFiles = os.listdir(from_dir)
    print(listFiles)

    for file_Name in listFiles:
        path1 = os.path.join(from_dir, file_Name)
        path2 = os.path.join(to_dir, "arquivos da pasta anterior")
        path3 = os.path.join(path2, file_Name)

        print(path1)
        print(path2)
        print(path3)
        
        if os.path.exists(path2):
            print("Movendo.." + file_Name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo.." + file_Name)
            shutil.move(path1, path3)
    
    value = input("Digite 'n' se quiser terminar o programa. Qualquer outra coisa se quiser mover mais arquivos. ")
    if value == "n":
        print("Encerrando o programa...")
        break
