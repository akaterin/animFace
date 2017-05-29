# 1, Inner brow riser: LeftInnerBrowUp, RightInnerBrowUp
# 2, Outer brow riser: LeftOuterBrowUp, RightOuterBrowUp,
# 4, Brow lowerer: LeftBrowDown, RightBrowDown,
# 5, Upper lid riser: LeftUpperLidOpen, RightUpperLidOpen
# 6, Cheek riser: LeftCheekUp, RightCheekUp
# 7, Lid tightener: LeftLowerLidUp, RightLowerLidUp
# 9, Nose wrinkler: NoseWrinkler
# 10, Upper Lip Riser: UpperLipUp
# 12, Lip corner puller: MouthLeftPullUp, MouthRightPullUp
# 14, Dimpler: MouthLeftPullSide, MouthLeftPullSide
# 15, Lop corner depressor: MouthLeftPullDown, MouthRightPullDown
# 17, Chin riser: ChinForward :( :( :(
# 20, Lip strecher: MouthLeftPullSide, MouthLeftPullSide
# 23, Lip tightener: LipKiss
# 25, Lips part: LowerLipDown
# 26, Jaw drop: JawDrop
# 28, Lip suck:lowerLipBackward, UpperLipBackward, lowerLipUp
# 45, Blink: LeftUpperLidClosed, RightUpperLidClosed

class AuBlenderMapper:

    def __init__(self):
        self.mappings = {
                '01': [('LeftInnerBrowUp', 1), ('RightInnerBrowUp', 1)],
                '02': [('LeftOuterBrowUp', 1), ('RightOuterBrowUp', 1)],
                '04': [('LeftBrowDown', 1), ('RightBrowDown', 1)],
                '05': [('LeftUpperLidOpen', 1), ('RightUpperLidOpen', 1)],
                '06': [('LeftCheekUp', 1), ('RightCheekUp', 1)],
                '07': [('LeftLowerLidUp', 1), ('RightLowerLidUp', 1)],
                '09': [('NoseWrinkler', 1)],
                '10': [('UpperLipUp', 1)],
                '12': [('MouthLeftPullUp', 1), ('MouthRightPullUp', 1)],
                '14': [('MouthLeftPullSide', 1), ('MouthRightPullSide', 1)],
                '15': [('MouthLeftPullDown', 1), ('MouthRightPullDown', 1)],
                '17': [('ChinForward', 1)],
                '20': [('MouthLeftPullSide', 1), ('MouthLeftPullSide', 1)],
                '23': [('LipKiss', 1)],
                '25': [('LowerLipDown', 1)],
                '26': [('JawDrop', 1)],
                '28': [('lowerLipBackward', 1), ('UpperLipBackward', 1), ('lowerLipUp', 1)],
                '45': [('LeftUpperLidClosed', 1), ('RightUpperLidClosed', 1)]
                }

    def map_au(self, au):
        return self.mappings[au]

