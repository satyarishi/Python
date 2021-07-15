import sys
import imdb

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
ia = imdb.IMDb()

search = ia.get_top250_movies()
for i in range(100):
    print(search[i])

sys.stdout = orig_stdout
f.close()
