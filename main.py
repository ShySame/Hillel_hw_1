import re


def parse(query: str) -> dict:
    dict = {}
    key, znach = re.findall(r'(\w+)=', query), re.findall(r'=(\w+)', query)
    for item1, item2 in zip(key, znach): dict.update({item1: item2})
    return dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    #========================================================================================================================================
    #-----------------------------------------------------------Dop_testi--------------------------------------------------------------------

    assert parse('https://example.com/path/to/page?color=purple&?name=ferret&zhuk&') == {'color': 'purple','name': 'ferret'}
    assert parse('https://example.com/path/to/page?name=ferret&color=pur&qukareku') == {'name': 'ferret','color': 'pur'}
    assert parse('http://example.com/name') == {}
    assert parse('http://example.com/path/to/page?name=ferret&color=purple/lop=tut') == {'name': 'ferret','color': 'purple','lop': 'tut'}
    assert parse('http://example.com/?name=Dima_Net') == {'name': 'Dima_Net'}
    assert parse('https://example.com/path/to/page?s=s/d=d/f=f/color=purple&?name=ferret&zhuk&') == {'s': 's','d': 'd','f': 'f',
                                                                                                     'color': 'purple','name': 'ferret'}
    assert parse('https://example.com/path/to/page?name=ferret1983&color=pur&qukareku') == {'name': 'ferret1983','color': 'pur'}
    assert parse('http://example.com/name=#=') == {}
    assert parse('http://example.com/path/to/page?name=ferret&color=purple/lop=tut20_20') == {'name': 'ferret','color': 'purple','lop': 'tut20_20'}
    assert parse('http://example.com/?name=Dima_Net&=&======') == {'name': 'Dima_Net'}


