#!/usr/bin/python
# -*- coding:utf-8 -*-  
# Author: 可达鸭不可达
# Create Date: 2021/3/8
import re
from collections import Counter


def count(file_name):
    # TODO 打开这个文件, 统计每个 单词  出现的次数, 返回dict; 如 {'hello': 10, 'world': 1}; 注意 man’s 这种也算一个单词
    # TODO with open(file_name, ...)
    # 提示: 用正则会快一点.
    # 给怡宝的提示: 怡宝可以用collection.Counter   (最好先不用, 自己做一次, 熟练以后可以用Counter)
    with open(file_name, 'r', encoding='utf-8') as f:
        all = f.readlines()
    alls = '\n'.join(all)
    r = re.findall(r'\w+[’]?[\w]*', alls)
    cc = Counter(r)
    return dict(cc)


if __name__ == '__main__':
    result = count('1.txt')

    true_result = {'Youth': 3, 'is': 25, 'not': 7, 'a': 27, 'time': 5, 'of': 66, 'life': 11, 'it': 13, 'state': 1,
                   'mind': 1, 'matter': 2, 'rosy': 1, 'cheeks': 1, 'red': 1, 'lips': 1, 'and': 36, 'supple': 1,
                   'knees': 1, 'the': 60, 'will': 2, 'quality': 1, 'imagination': 1, 'vigor': 2, 'emotions': 1,
                   'freshness': 1, 'deep': 1, 'springs': 1, 'means': 1, 'temperamental': 1, 'predominance': 1,
                   'courage': 2, 'over': 2, 'timidity': 1, 'appetite': 2, 'for': 11, 'adventure': 1, 'love': 4,
                   'ease': 1, 'This': 1, 'often': 6, 'exists': 1, 'in': 24, 'man': 3, '60': 2, 'more': 5, 'than': 1,
                   'boy': 1, '20': 2, 'Nobody': 1, 'grows': 1, 'old': 5, 'merely': 1, 'by': 9, 'number': 1, 'years': 2,
                   'We': 5, 'grow': 1, 'deserting': 1, 'our': 5, 'ideals': 1, 'Years': 1, 'may': 4, 'wrinkle': 1,
                   'skin': 1, 'but': 8, 'to': 14, 'give': 1, 'up': 2, 'enthusiasm': 1, 'wrinkles': 1, 'soul': 1,
                   'Worry': 1, 'fear': 1, 'self': 1, 'distrust': 1, 'bows': 1, 'heart': 4, 'turns': 1, 'spirit': 2,
                   'back': 2, 'dust': 1, 'Whether': 1, 'or': 6, '16': 1, 'there': 4, 'every': 1, 'human': 3,
                   'being’s': 1, 'lure': 1, 'wonders': 1, 'unfailing': 1, 'what’s': 1, 'next': 1, 'joy': 1, 'game': 1,
                   'living': 2, 'In': 2, 'center': 1, 'your': 4, 'my': 3, 'wireless': 1, 'station': 1, 'so': 2,
                   'long': 5, 'as': 22, 'receives': 2, 'messages': 1, 'beauty': 1, 'hope': 2, 'power': 1, 'from': 3,
                   'infinite': 1, 'you': 2, 'are': 10, 'young': 2, 'When': 2, 'aerials': 2, 'down': 1, 'covered': 1,
                   'with': 10, 'snows': 1, 'cynicism': 1, 'ice': 1, 'pessimism': 1, 'then': 2, 'you’ve': 1, 'grown': 1,
                   'even': 2, 'at': 4, 'catch': 1, 'waves': 1, 'optimism': 1, 'there’s': 1, 'die': 4, '80': 1,
                   'Three': 1, 'Days': 1, 'See': 1, 'All': 1, 'us': 11, 'have': 11, 'read': 1, 'thrilling': 1,
                   'stories': 3, 'which': 7, 'hero': 3, 'had': 1, 'only': 3, 'limited': 1, 'specified': 1, 'live': 6,
                   'Sometimes': 2, 'was': 3, 'year': 1, 'sometimes': 2, 'short': 1, '24': 1, 'hours': 3, 'But': 4,
                   'always': 5, 'we': 15, 'were': 4, 'interested': 1, 'discovering': 1, 'just': 2, 'how': 1,
                   'doomed': 2, 'chose': 1, 'spend': 1, 'his': 5, 'last': 4, 'days': 4, 'I': 4, 'speak': 1, 'course': 2,
                   'free': 1, 'men': 3, 'who': 5, 'choice': 1, 'condemned': 1, 'criminals': 1, 'whose': 1, 'sphere': 1,
                   'activities': 1, 'strictly': 1, 'delimited': 1, 'Such': 2, 'set': 1, 'thinking': 1, 'wondering': 1,
                   'what': 7, 'should': 5, 'do': 3, 'under': 1, 'similar': 1, 'circumstances': 1, 'What': 2,
                   'events': 1, 'experiences': 1, 'associations': 1, 'crowd': 1, 'into': 3, 'those': 5, 'mortal': 1,
                   'beings': 1, 'regrets': 1, 'thought': 3, 'would': 7, 'be': 7, 'an': 6, 'excellent': 1, 'rule': 1,
                   'each': 5, 'day': 4, 'if': 4, 'tomorrow': 1, 'attitude': 2, 'emphasize': 1, 'sharply': 1,
                   'values': 3, 'gentleness': 1, 'keenness': 1, 'appreciation': 2, 'lost': 2, 'when': 2, 'stretches': 1,
                   'before': 1, 'constant': 2, 'panorama': 1, 'months': 1, 'come': 1, 'There': 2, 'adopt': 1,
                   'Epicurean': 1, 'motto': 1, 'Eat': 1, 'drink': 1, 'merry': 1, 'most': 4, 'people': 1, 'chastened': 1,
                   'certainty': 1, 'impending': 1, 'death': 3, 'usually': 3, 'saved': 1, 'minute': 1, 'some': 2,
                   'stroke': 1, 'fortune': 1, 'almost': 1, 'sense': 1, 'changed': 1, 'He': 1, 'becomes': 2,
                   'appreciative': 2, 'meaning': 1, 'its': 2, 'permanent': 1, 'spiritual': 1, 'It': 7, 'has': 1,
                   'been': 2, 'noted': 1, 'that': 7, 'lived': 2, 'shadow': 1, 'bring': 2, 'mellow': 1, 'sweetness': 1,
                   'everything': 1, 'they': 7, 'Most': 1, 'however': 1, 'take': 2, 'granted': 1, 'know': 1, 'one': 2,
                   'must': 1, 'picture': 1, 'far': 2, 'future': 1, 'buoyant': 1, 'health': 2, 'all': 3,
                   'unimaginable': 1, 'seldom': 2, 'think': 3, 'The': 6, 'stretch': 1, 'out': 3, 'endless': 1,
                   'vista': 1, 'So': 1, 'go': 1, 'about': 1, 'petty': 1, 'tasks': 1, 'hardly': 1, 'aware': 1,
                   'listless': 1, 'toward': 1, 'same': 4, 'lethargy': 1, 'am': 1, 'afraid': 1, 'characterizes': 1,
                   'use': 2, 'faculties': 2, 'senses': 1, 'Only': 1, 'deaf': 2, 'appreciate': 1, 'hearing': 3,
                   'blind': 2, 'realize': 1, 'manifold': 1, 'blessings': 1, 'lie': 1, 'sight': 4, 'Particularly': 1,
                   'does': 2, 'this': 3, 'observation': 1, 'apply': 1, 'adult': 2, 'never': 2, 'suffered': 1,
                   'impairment': 1, 'make': 2, 'fullest': 1, 'these': 1, 'blessed': 1, 'Their': 1, 'eyes': 1, 'ears': 1,
                   'sights': 1, 'sounds': 1, 'hazily': 1, 'without': 1, 'concentration': 1, 'little': 1, 'story': 1,
                   'being': 3, 'grateful': 1, 'until': 2, 'lose': 1, 'conscious': 1, 'ill': 1, 'blessing': 1,
                   'stricken': 1, 'few': 1, 'during': 1, 'early': 1, 'Darkness': 1, 'him': 3, 'silence': 1, 'teach': 1,
                   'joys': 1, 'sound': 1, 'Companionship': 1, 'Books': 3, 'A': 3, 'known': 1, 'books': 6, 'he': 3,
                   'reads': 1, 'well': 2, 'company': 2, 'keeps': 1, 'companionship': 1, 'best': 6, 'whether': 1,
                   'good': 5, 'book': 6, 'among': 1, 'friends': 1, 'today': 2, 'change': 1, 'patient': 1, 'cheerful': 1,
                   'companions': 2, 'turn': 1, 'upon': 1, 'times': 1, 'adversity': 1, 'distress': 1, 'kindness': 1,
                   'amusing': 1, 'instructing': 1, 'youth': 1, 'comforting': 1, 'consoling': 1, 'age': 1, 'Men': 2,
                   'discover': 2, 'their': 5, 'affinity': 1, 'other': 2, 'mutual': 1, 'two': 1, 'persons': 1,
                   'friend': 1, 'admiration': 1, 'both': 1, 'entertain': 1, 'third': 1, 'proverb': 1, 'Love': 2,
                   'me': 2, 'dog': 1, 'wisdom': 1, 'truer': 1, 'higher': 1, 'bond': 1, 'union': 1, 'can': 2, 'feel': 2,
                   'sympathize': 2, 'through': 2, 'favorite': 1, 'author': 1, 'They': 2, 'together': 1, 'them': 5,
                   'urn': 1, 'enshrining': 1, 'could': 1, 'world': 3, 'man’s': 1, 'part': 1, 'thoughts': 3, 'Thus': 1,
                   'treasuries': 1, 'words': 1, 'golden': 1, 'remembered': 1, 'cherished': 1, 'become': 1,
                   'comforters': 1, 'possess': 1, 'essence': 1, 'immortality': 1, 'lasting': 1, 'products': 2,
                   'effort': 1, 'Temples': 1, 'statues': 1, 'decay': 1, 'survive': 2, 'Time': 1, 'no': 1, 'account': 1,
                   'great': 2, 'fresh': 1, 'first': 1, 'passed': 1, 'author’s': 1, 'minds': 2, 'ages': 1, 'ago': 1,
                   'said': 2, 'still': 2, 'speaks': 1, 'vividly': 1, 'ever': 2, 'printed': 1, 'page': 1, 'effect': 1,
                   'sift': 1, 'bad': 1, 'nothing': 1, 'literature': 1, 'e': 1, 'really': 2, 'introduce': 1,
                   'society': 1, 'presence': 1, 'greatest': 1, 'hear': 1, 'did': 1, 'see': 1, 'alive': 1, 'enjoy': 1,
                   'grieve': 1, 'experience': 1, 'ours': 1, 'measure': 1, 'actors': 1, 'scenes': 1, 'describe': 1,
                   'Embalmed': 1, 'spirits': 1, 'walk': 1, 'abroad': 1, 'voice': 1, 'intellect': 1, 'on': 1,
                   'listens': 1}

    assert result == true_result
