import numpy as np

class ExtractAus:

    def extract_aus(self, file):
        data = np.loadtxt(file, delimiter=',', skiprows=1)
        au_data = data[:, 396:]
        au_intensity = au_data[:, :17]
        au_presence = au_data[:, 17:]
        labels = np.loadtxt(file, delimiter=',', dtype=str)
        labels = labels[0, 396:]
        result = []
        for frame_no, frame in enumerate(au_intensity):
            print("Frame: {0}.".format(frame_no))
            frame_aus = []
            for i, au_value in enumerate(frame):
                if au_presence[frame_no][i] != 0:
                    label = labels[i][3:-3].strip()[2:]
                    au = (label, au_value/5.0)
                    print("{0}: {1}".format(au[0], au[1]))
                    frame_aus.append(au)
            result.append(frame_aus)
        return result

