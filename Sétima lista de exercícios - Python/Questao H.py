# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'
def first_half(s):
    return s[:int(len(s)/2)]
