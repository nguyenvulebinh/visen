import ftfy
import bogo
import re

map_char = {
    "à": ["a", "f"], "á": ["a", "s"], "â": ["aa", ""], "ã": ["a", "x"], "è": ["e", "f"], "é": ["e", "s"],
    "ê": ["ee", ""], "ì": ["i", "f"], "í": ["i", "s"], "ò": ["o", "f"], "ó": ["o", "s"], "ô": ["oo", ""],
    "õ": ["o", "x"], "ù": ["u", "f"], "ú": ["u", "s"], "ý": ["y", "s"], "ă": ["aw", ""], "ĩ": ["i", "x"],
    "ũ": ["u", "x"], "ơ": ["ow", ""], "ư": ["uw", ""], "ạ": ["a", "j"], "ả": ["a", "r"], "ấ": ["aa", "s"],
    "ầ": ["aa", "f"], "ẩ": ["aa", "r"], "ẫ": ["aa", "x"], "ậ": ["aa", "j"], "ắ": ["aw", "s"], "ằ": ["aw", "f"],
    "ẳ": ["aw", "r"], "ẵ": ["aw", "x"], "ặ": ["aw", "j"], "ẹ": ["e", "j"], "ẻ": ["e", "r"], "ẽ": ["e", "x"],
    "ế": ["ee", "s"], "ề": ["ee", "f"], "ể": ["ee", "r"], "ễ": ["ee", "x"], "ệ": ["ee", "j"], "ỉ": ["i", "r"],
    "ị": ["i", "j"], "ọ": ["o", "j"], "ỏ": ["o", "r"], "ố": ["oo", "s"], "ồ": ["oo", "f"], "ổ": ["oo", "r"],
    "ỗ": ["oo", "x"], "ộ": ["oo", "j"], "ớ": ["ow", "s"], "ờ": ["ow", "f"], "ở": ["ow", "r"], "ỡ": ["ow", "x"],
    "ợ": ["ow", "j"], "ụ": ["u", "j"], "ủ": ["u", "r"], "ứ": ["uw", "s"], "ừ": ["uw", "f"], "ử": ["uw", "r"],
    "ữ": ["uw", "x"], "ự": ["uw", "j"], "ỳ": ["y", "f"], "ỵ": ["y", "j"], "ỷ": ["y", "r"], "ỹ": ["y", "x"],
    "đ": ["dd", ""],
    "À": ["A", "f"], "Á": ["A", "s"], "Â": ["AA", ""], "Ã": ["A", "x"], "È": ["E", "f"], "É": ["E", "s"],
    "Ê": ["EE", ""], "Ì": ["I", "f"], "Í": ["I", "s"], "Ò": ["O", "f"], "Ó": ["O", "s"], "Ô": ["OO", ""],
    "Õ": ["O", "x"], "Ù": ["U", "f"], "Ú": ["U", "s"], "Ý": ["Y", "s"], "Ă": ["AW", ""], "Đ": ["DD", ""],
    "Ĩ": ["I", "x"], "Ũ": ["U", "x"], "Ơ": ["OW", ""], "Ư": ["UW", ""], "Ạ": ["A", "j"], "Ả": ["A", "r"],
    "Ấ": ["AA", "s"], "Ầ": ["AA", "f"], "Ẩ": ["AA", "r"], "Ẫ": ["AA", "x"], "Ậ": ["AA", "j"],
    "Ắ": ["AW", "s"], "Ằ": ["AW", "f"], "Ẳ": ["AW", "r"], "Ẵ": ["AW", "x"], "Ặ": ["AW", "j"],
    "Ẹ": ["E", "j"], "Ẻ": ["E", "r"], "Ẽ": ["E", "x"], "Ế": ["EE", "s"], "Ề": ["EE", "f"], "Ể": ["EE", "r"],
    "Ễ": ["EE", "x"], "Ệ": ["EE", "j"], "Ỉ": ["I", "r"], "Ị": ["I", "j"], "Ọ": ["O", "j"], "Ỏ": ["O", "r"],
    "Ố": ["OO", "s"], "Ồ": ["OO", "f"], "Ổ": ["OO", "r"], "Ỗ": ["OO", "x"], "Ộ": ["OO", "j"],
    "Ớ": ["OW", "s"], "Ờ": ["OW", "f"], "Ở": ["OW", "r"], "Ỡ": ["OW", "x"], "Ợ": ["OW", "j"],
    "Ụ": ["U", "j"], "Ủ": ["U", "r"], "Ứ": ["UW", "s"], "Ừ": ["UW", "f"], "Ử": ["UW", "r"], "Ữ": ["UW", "x"],
    "Ự": ["UW", "j"], "Ỳ": ["Y", "f"], "Ỵ": ["Y", "j"], "Ỷ": ["Y", "r"], "Ỹ": ["Y", "x"]
}

raw_char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMàáâãèéêìíòóôõùúýăĩũơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉ' \
           'ịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝĂĐĨŨƠƯẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼẾỀỂỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴỶỸ'

intab_l = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
intab_u = "ẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
intab = [ch for ch in intab_l + intab_u]

outtab_l = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d"
outtab_u = "A" * 17 + "O" * 17 + "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D"
outtab = outtab_l + outtab_u

subword_split = re.compile(r'([^{}])'.format(re.escape(raw_char)))
set_map_char = set(map_char.keys())

r = re.compile("|".join(intab))
replaces_dict_remove = dict(zip(intab, outtab))


def remove_tone(utf8_str):
    return r.sub(lambda m: replaces_dict_remove[m.group(0)], utf8_str)


def get_char_code(chr):
    if chr in map_char:
        return map_char[chr]
    else:
        return [chr, '']


def get_enter_code(word):
    word_char = []
    word_tone = []
    for chr in list(word):
        chars, tone = get_char_code(chr)
        word_char += chars
        word_tone += tone
    return ''.join(word_char) + ''.join(word_tone)[-1:]


def clean_tone(str_in):
    str_in = ftfy.fix_text(str_in)
    typing_out = []
    for word in str_in.split():
        if len(set_map_char & set(list(word))) == 0:
            typing_out.append(word)
        else:
            sub_words = subword_split.split(word)
            for i in range(len(sub_words)):
                if len(set_map_char & set(list(sub_words[i]))) != 0:
                    # if after bogo == before bogo, using raw input
                    sub_word_enter = get_enter_code(sub_words[i])
                    sub_word_no_tone = remove_tone(sub_words[i])
                    sub_word_bogo = bogo.process_sequence(sub_word_enter)
                    sub_word_bogo_enter = get_enter_code(sub_word_bogo)
                    sub_word_bogo_no_tone = remove_tone(sub_word_bogo)
                    if sub_word_bogo != sub_word_enter and \
                            sub_word_bogo_no_tone == sub_word_no_tone and \
                            sub_word_bogo_enter == sub_word_enter:
                        sub_words[i] = sub_word_bogo
            typing_out.append(''.join(sub_words))

    return " ".join(typing_out)
