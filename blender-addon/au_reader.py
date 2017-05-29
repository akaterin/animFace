import numpy as np

class AuReader(object):

    def read(self, file):
        data = np.loadtxt(file)
        return data

if __name__ == "__main__":
    reader = AuReader()
    data = reader.read('../face-units-extractor/output.txt')
    print(data)
