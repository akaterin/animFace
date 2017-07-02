import os

movies = os.listdir('movies/')
for movie in movies:
  command = "~/Studies/openface/OpenFace/bin/FeatureExtraction -f movies/{0} -outroot open-face-outputs -of '{1}2.txt' -q".format(movie, movie.split('.')[0])
  os.system(command)