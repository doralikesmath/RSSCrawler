"""
                                ╔═════════════════════════════════════════════╗
                                ║             .-') _                          ║
                                ║            (  OO) )                         ║
                                ║          ,(_)----. .---. .-----.            ║
                                ║          |       |/_   |/  -.   \           ║
                                ║          '--.   /  |   |'-' _'  |           ║
                                ║          (_/   /   |   |   |_  <            ║
                                ║           /   /___ |   |.-.  |  |           ║
                                ║          |        ||   |\ `-'   /           ║
                                ║          `--------'`---' `----''     ©2021  ║
                                ╚═════════════════════════════════════════════╝
"""
import unicodedata


DECOMPOSED = [
    ['à', 'à'],
    ['á', 'á'],
    ['ã', 'ã'],
    ['ả', 'ả'],
    ['ạ', 'ạ'],
    ['è', 'è'],
    ['é', 'é'],
    ['ẽ', 'ẽ'],
    ['ẻ', 'ẻ'],
    ['ẹ', 'ẹ'],
    ['ì', 'ì'],
    ['í', 'í'],
    ['ĩ', 'ĩ'],
    ['ỉ', 'ỉ'],
    ['ị', 'ị'],
    ['ò', 'ò'],
    ['ó', 'ó'],
    ['õ', 'õ'],
    ['ỏ', 'ỏ'],
    ['ọ', 'ọ'],
    ['ờ', 'ờ'],
    ['ớ', 'ớ'],
    ['ỡ', 'ỡ'],
    ['ở', 'ở'],
    ['ợ', 'ợ'],
    ['ù', 'ù'],
    ['ú', 'ú'],
    ['ũ', 'ũ'],
    ['ủ', 'ủ'],
    ['ụ', 'ụ'],
    ['ỳ', 'ỳ'],
    ['ý', 'ý'],
    ['ỹ', 'ỹ'],
    ['ỷ', 'ỷ'],
    ['ỵ', 'ỵ'],
    ['â', 'â'],
    ['ầ', 'ầ'],
    ['ấ', 'ấ'],
    ['ẫ', 'ẫ'],
    ['ẩ', 'ẩ'],
    ['ậ', 'ậ'],
    ['ằ', 'ằ'],
    ['ắ', 'ắ'],
    ['ẵ', 'ẵ'],
    ['ẳ', 'ẳ'],
    ['ặ', 'ặ'],
    ['ừ', 'ừ'],
    ['ứ', 'ứ'],
    ['ữ', 'ữ'],
    ['ử', 'ử'],
    ['ự', 'ự'],
    ['ê', 'ê'],
    ['ề', 'ề'],
    ['ế', 'ế'],
    ['ễ', 'ễ'],
    ['ể', 'ể'],
    ['ệ', 'ệ'],
    ['ô', 'ô'],
    ['ồ', 'ồ'],
    ['ố', 'ố'],
    ['ỗ', 'ỗ'],
    ['ổ', 'ổ'],
    ['ộ', 'ộ']
]


NORMALIZE = [
    ["òa", "oà"],
    ["óa", "oá"],
    ["ỏa", "oả"],
    ["õa", "oã"],
    ["ọa", "oạ"],
    ["òe", "oè"],
    ["óe", "oé"],
    ["ỏe", "oẻ"],
    ["õe", "oẽ"],
    ["ọe", "oẹ"],
    ["ùy", "uỳ"],
    ["úy", "uý"],
    ["ủy", "uỷ"],
    ["ũy", "uỹ"],
    ["ụy", "uỵ"],
    ["Ủy", "Uỷ"]
]


SPECIAL_IA = [
    ["ia", "ia"],
    ["ía", "iá"],
    ["ìa", "ià"],
    ["ỉa", "iả"],
    ["ĩa", "iã"],
    ["ịa", "iạ"]
]


SPECIAL_UA = [
    ["ua", "ua"],
    ["úa", "uá"],
    ["ùa", "uà"],
    ["ủa", "uả"],
    ["ũa", "uã"],
    ["ụa", "uạ"]
]


def to_precomposed(text):
    for i in range(len(DECOMPOSED)):
        text = text.replace(DECOMPOSED[i][0], DECOMPOSED[i][1])
    return text


def normalize_tone_marks(text):
    # easy cases
    for i in range(len(NORMALIZE)):
        text = text.replace(NORMALIZE[i][0], NORMALIZE[i][1])
    # special cases
    words = text.split(" ")
    for j in range(len(words)):
        for i in range(len(SPECIAL_IA)):
            if SPECIAL_IA[i][0] in text:
                if words[j][0] == 'g':
                    words[j] = words[j].replace(SPECIAL_IA[i][0], SPECIAL_IA[i][1])
                    break

            if SPECIAL_IA[i][1] in text:
                if words[j][0] != 'g':
                    words[j] = words[j].replace(SPECIAL_IA[i][1], SPECIAL_IA[i][0])
                    break

            if SPECIAL_UA[i][0] in text:
                if words[j][0] == 'q':
                    words[j] = words[j].replace(SPECIAL_UA[i][0], SPECIAL_UA[i][1])
                    break

            if SPECIAL_UA[i][1] in text:
                if words[j][0] != 'q':
                    words[j] = words[j].replace(SPECIAL_UA[i][1], SPECIAL_UA[i][0])
                    break
    text = " ".join(words)
    return text


if __name__=="__main__":
    print(normalize_tone_marks("họa"))
    print(normalize_tone_marks("quá"))
    print(normalize_tone_marks("qúa"))
    print(normalize_tone_marks("múa"))
    print(normalize_tone_marks("muà"))