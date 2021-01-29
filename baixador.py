import wget


links = open('chaves.txt', 'r')
def download():
    for link in range(0,3):
        url = links.readline()
        wget.download(url, f'/Users/fmore/Documents/Pycharm/foto{link}.jpg')
        print('Baixou: ', url)

print('#' * 10)
print('ARCHIVE DOWNLOADER v0.2')
print('#' * 10)
resposta = input('Deseja Iniciar? S/n: ')
if resposta == 'sim' or resposta == 's':
    print('Iniciando...')
    download()
else:
    quit()
