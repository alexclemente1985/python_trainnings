from mhyt import yt_download

def teste():
    url = 'https://www.youtube.com/watch?v=10pujTAd13Y&list=PLifTOxQosMmPWaBAxjZtdg-yzjI7H_rFA'
    file = 'gerenciador.mp4'

    yt_download(url, file)

if __name__ == '__main__':
    teste()