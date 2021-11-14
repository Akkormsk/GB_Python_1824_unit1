import re


def email_parse(email_adress):
    d = {}
    re_list = re.compile("^(.+)[@]{1}(\w+[/.]{1}\w+)$", re.IGNORECASE).findall(email_adress)
    if re_list:
        d['username'] = re_list[0][0]
        d['domain'] = re_list[0][1]
    else:
        raise ValueError(f'Wrong email: {email_adress}')
    return d


if __name__ == '__main__':
    import sys

    print(email_parse(sys.argv[1]))
