# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:36:11 2023
@author: Tarun Luthra

Commented by Torin Kearney for Cryptography final
"""

message = 'PTN LRYYBJSVA' #encrypted message, ENSURE ALL UPPERCASE AND NO {}
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(Letters)):
   translated = ''
   for ch in message:
      if ch in Letters:
         num = Letters.find(ch)
         num = num - key
         if num < 0:
            num = num + len(Letters)
         translated = translated + Letters[num]
      else:
         translated = translated + ch
   print('Hacking key is %s: %s' % (key, translated))

#will bruteforce all keys from 1-25, then you need to pick the one that makes the most sense