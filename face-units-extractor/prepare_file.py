from extract_aus import ExtractAus
from mapping import AuBlenderMapper
import numpy as np

class FilePreparer:

    def __init__(self):
        self.extractor = ExtractAus()
        self.mapper = AuBlenderMapper()

    def prepare(self, file):
        aus = self.extractor.extract_aus(file)
        result = []
        for frame in aus:
            frame_result = []
            for au in frame:
                label, value = au
                mapping = self.mapper.map_au(label)
                for mapped_au in mapping:
                    au_result = (mapped_au[0], mapped_au[1]*value)
                    frame_result.append(au_result)
            result.append(frame_result)
        result = np.array(result)
        return result

if __name__ == "__main__":
    fp = FilePreparer()
    fp.prepare('test.txt')


