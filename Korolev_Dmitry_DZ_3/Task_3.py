from collections import defaultdict


def thesaurus(*args):
    letters = []
    people = []
    for name in list(args):
        letters.append(list(name)[0])
        myset = set(letters)
    for letter in myset:
        ll = [a for a in list(args) if list(a)[0] == letter]
        people.append(ll)
    return dict(zip(myset, list(people)))


def thesaurus_adv(*args):
    arg_dict = {}
    dicts = []
    for arg in list(args):
        name = arg.split()
        arg_dict.update({arg: name[1][0]})
    last_l = set(arg_dict.values())
    for lett in last_l:
        ll = [pers for pers in arg_dict if arg_dict[pers] == lett]
        dicts.append(thesaurus(*ll))
    res_dict = dict(zip(last_l, dicts))
    return res_dict


print(thesaurus('Jimmy Hendrix', 'Brad Pitt', 'Paul Smith', 'Jake Paul'))
print(thesaurus_adv('Jimmy Hendrix', 'Brad Pitt', 'Paul Smith', 'Harry Potter', 'Richard Gere', 'Tom Hanks', 'Har Pot', 'Peter Soulman'))
