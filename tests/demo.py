from pip._vendor.distlib.compat import raw_input


def i():
    d = {'1234': '8.8.8.8', '2345': '0.0.0.0', '3213': '4.4.4.4', '4523': '1.1.1.1', '7654': '1.3.3.7',
         '9999': '127.0.0.1'}
    ch = raw_input('Pleasure Enter your choice : ')
    keys = d.keys()
    values = d.values()
    # print keys, values
    # for k, v in d.items():
    #     if k == ch:
    #         ind = d.keys().index(k)
    #         print
    #         keys[ind - 1], ':', values[ind - 1]
    #         print
    #         keys[ind + 1], ':', values[ind + 1]


def get_shifted_key() :
    pos = 0
    d = {'aaaa': 'a', 'bbbb': 'b', 'cccc': 'c', 'dddd': 'd', 'eeee': 'e', 'ffff': 'f'}

    for i in d:
        pos += 1
        if i == 'cccc':
            listForm = list(d.values())
            print(listForm[pos - 1])
            print(listForm[pos + 1])


if __name__ == "__main__":
    get_shifted_key()
