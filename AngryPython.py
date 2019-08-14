# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:59:34 2017

@author: Damien Rigden

ANGRY PYTHON
"""

s = "Ok, I figured it out. I know why the code needs this string."
var3 = 0
var4 = 0
var5 = s[3]

for x in range(len(eval(s[46]))):
    var5 += s[:-x]
    if len(var5) >= 50:
        var4 += len(s)//30
        var3 -= 4
    var3 += 7
var4 //= 2 - 7

print(var5[-var3] + var5[var3] + var5[var3//2-var4-var4-var4-9] + \
      s[abs(var4)] + s[var4] + var5[var4//var4+31] + s[len(var5)//len(s)-3] + \
      var5[var3])
