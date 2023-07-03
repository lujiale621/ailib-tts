import re
import cn2an
import opencc
import config

converter = opencc.OpenCC(config.ABS_PATH + '/chinese_dialect_lexicons/jyutjyu_2')

# List of (Latin alphabet, ipa) pairs:
_latin_to_ipa = [(re.compile('%s' % x[0]), x[1]) for x in [
    ('A', 'ei˥'),
    ('B', 'biː˥'),
    ('C', 'siː˥'),
    ('D', 'tiː˥'),
    ('E', 'iː˥'),
    ('F', 'e˥fuː˨˩'),
    ('G', 'tsiː˥'),
    ('H', 'ɪk̚˥tsʰyː˨˩'),
    ('I', 'ɐi˥'),
    ('J', 'tsei˥'),
    ('K', 'kʰei˥'),
    ('L', 'e˥llou˨˩'),
    ('M', 'ɛːm˥'),
    ('N', 'ɛːn˥'),
    ('O', 'ou˥'),
    ('P', 'pʰiː˥'),
    ('Q', 'kʰiːu˥'),
    ('R', 'aː˥lou˨˩'),
    ('S', 'ɛː˥siː˨˩'),
    ('T', 'tʰiː˥'),
    ('U', 'juː˥'),
    ('V', 'wiː˥'),
    ('W', 'tʊk̚˥piː˥juː˥'),
    ('X', 'ɪk̚˥siː˨˩'),
    ('Y', 'waːi˥'),
    ('Z', 'iː˨sɛːt̚˥')
]]

_symbols_to_chinese = [(re.compile(f'{x[0]}'), x[1]) for x in [
    ('([0-9]+(?:\.?[0-9]+)?)%', r'百分之\1'),
    ('([0-9]+)/([0-9]+)', r'\2分之\1'),
    ('\+', r'加'),
    ('([0-9]+)-([0-9]+)', r'\1减\2'),
    ('×', r'乘以'),
    ('([0-9]+)x([0-9]+)', r'\1乘以\2'),
    ('([0-9]+)\*([0-9]+)', r'\1乘以\2'),
    ('÷', r'除以'),
    ('=', r'等于'),
    ('≠', r'不等于'),
]]


def symbols_to_chinese(text):
    for regex, replacement in _symbols_to_chinese:
        text = re.sub(regex, replacement, text)
    return text


def number_to_cantonese(text):
    return re.sub(r'\d+(?:\.?\d+)?', lambda x: cn2an.an2cn(x.group()), text)


def latin_to_ipa(text):
    for regex, replacement in _latin_to_ipa:
        text = re.sub(regex, replacement, text)
    return text


def cantonese_to_ipa(text):
    text = symbols_to_chinese(text)
    text = number_to_cantonese(text.upper())
    text = converter.convert(text).replace('-', '').replace('$', ' ')
    text = re.sub(r'[A-Z]', lambda x: latin_to_ipa(x.group()) + ' ', text)
    text = re.sub(r'[、；：]', '，', text)
    text = re.sub(r'\s*，\s*', ', ', text)
    text = re.sub(r'\s*。\s*', '. ', text)
    text = re.sub(r'\s*？\s*', '? ', text)
    text = re.sub(r'\s*！\s*', '! ', text)
    text = re.sub(r'\s*$', '', text)
    return text
