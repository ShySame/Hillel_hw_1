import re


def parse_cookie(query: str) -> dict:
    dict = {}
    key, znach = re.findall(r'(\w+)(.+?);', query), re.findall(r'=(\w*(?:=\w+)?);', query)
    for item2, item1 in zip(znach, key):
        dict.update({item1[0]: item2})
    return dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    """"""

    #========================================================================================================================================
    #-----------------------------------------------------------Dop_testi--------------------------------------------------------------------

    assert parse_cookie('name=Dima;;;=;') == {'name': 'Dima'}
    assert parse_cookie('wegerhnrj=grwg') == {}
    assert parse_cookie('name=Dima;age=28;ui') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;gender=helicopter;') == {'name': 'Dima=User', 'age': '28','gender':'helicopter'}
    assert parse_cookie('name=Ne_Dima;') == {'name': 'Ne_Dima'}
    assert parse_cookie(';') == {}
    assert parse_cookie('28;') == {}
    assert parse_cookie('nam=0;py=py;') == {'nam': '0','py': 'py'}
    assert parse_cookie(';name;Dima;') == {}
    assert parse_cookie('286=38;lyftydtky') == {'286':'38'}


