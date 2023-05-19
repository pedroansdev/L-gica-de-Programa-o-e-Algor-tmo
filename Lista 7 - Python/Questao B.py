# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
    resultado = ''
    for c in range(len(s)):
        resultado += s[:c]
    resultado += s
    return resultado
