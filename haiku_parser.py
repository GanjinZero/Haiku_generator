import MeCab
from romaji_kana import to_kana

def haiku_parser(sentence):
    mecab = MeCab.Tagger("-Ochasen")
    parse_result = mecab.parse(sentence).split('\n')
    result = ''
    for i in range(len(parse_result) - 2):
        parse_now = parse_result[i].split('\t')
        word = parse_now[0]
        hatsuon = parse_now[1]
        if hatsuon == '*':
            hatsuon = word
        result += hatsuon

    if len(result) == 17:
        print(result[0:5])
        print(result[5:12])
        print(result[12:17])
        return result
    return None

def haiku_parser_romaji(sentence):
    result = "".join(to_kana(sentence).split(" "))
    if len(result) == 17:
        print(result[0:5])
        print(result[5:12])
        print(result[12:17])
        return result
    return None

if __name__ == "__main__":
    print(haiku_parser('秋風の山をまはるや鐘の声'))
    print(haiku_parser_romaji('akikaze no yama o mawaru ya kane no koe'))