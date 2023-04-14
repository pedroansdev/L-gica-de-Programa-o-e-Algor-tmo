# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  
def extra_end(s):
    return 3 * s[-2:]
