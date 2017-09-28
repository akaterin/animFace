import os

movies = os.listdir('movies/friends')
for movie in movies:
  command = "~/Studies/openface/OpenFace/bin/FeatureExtraction -f movies/friends/{0} -outroot open-face-outputs -of '{1}.txt' -q".format(movie, movie.split('.')[0])
  os.system(command)
