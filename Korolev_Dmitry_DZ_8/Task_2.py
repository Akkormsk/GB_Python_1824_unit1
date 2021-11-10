import re


def logs_parse(logs_file):
    re_pattern = re.compile(r"^((?:\d+[.]){3}\d+)\s[-\s]{4}[\[](.+)[\]]\s[\"](\w+)\s(.+?)[\"]\s(\d+)\s(\d+)")
    for line in logs_file.readlines()[:50]:
        parsed_raw = re_pattern.findall(line)[0]
        print(parsed_raw)
    return


if __name__ == '__main__':
    with open('nginx_logs.txt') as f:
        logs_parse(f)
