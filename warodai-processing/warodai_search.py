with open('D:\Документы\Python\warodai.txt', 'r', encoding='utf-16') as warodai:
    war_str = ''.join(warodai.readlines())

    sample = war_str.split('\n\n')[1:]

    sample_struct = list(map(lambda x: [x.split('\n')[0], x.split('\n')[1:]], sample))
    # [0] => word; [1][0] => translate (main meaning); [1][1:] => examples (other meanings)

    get_pronunciation = lambda s: s.split('(')[1].split(')')[0].replace(':', '')

    result = list(filter(lambda s: any(get_pronunciation(s[0]) in meaning and len(get_pronunciation(s[0])) >= 4 for meaning in s[1]), sample_struct))

    print(len(result))

with open('D:\Документы\Python\warodai_processed.txt', 'w', encoding='utf-16') as war_save:
    war_save.writelines('\n\n'.join(map(lambda s: '\n'.join([s[0]] + s[1]), result)))