class Solution:
    def romanos_to_int(s):
        numero = 0
        romanos = {'I':1 , 'V':5, 'X':10, 'L':50, 'C':100, 'D' :500, 'M':1000}

        for i in range(len(s)):
            if i > 0 and romanos[s[i]] > romanos[s[i-1]]:
                numero += romanos[s[i]] - 2 * romanos[s[i-1]]
            else:
                numero += romanos[s[i]]
    
        return numero

    entrada = input()
    print(romanos_to_int(entrada)) 