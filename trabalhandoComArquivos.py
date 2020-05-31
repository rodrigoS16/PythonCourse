# para abrir um arquivo open("D:\CursoC#\FileStream\SalesFile.csv", mode="r")
# sendo open("<caminho do arquivo + nome e extensão", modo de manipulação

arquivo = open("D:\Python_CodesSaved\FileStream\palavras.txt", "w")
arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.close();

arquivo = open("D:\Python_CodesSaved\FileStream\palavras.txt", "a")
arquivo.write("morango\n")
arquivo.write("maça\n")
arquivo.close()