#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamourl

02b dan diachi githubbailamourl tu trang web duoiday
    https://forms.gle/s46X7pPDY7p79NQr5

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333, and 4444!
"""
#endregion debai

#region bailam

def hi(*args): 
   if not args or all(arg == None for arg in args) or all(arg == '' for arg in args):
      return 'Hi!'
   valid_args = [arg for arg in args if arg] 
   if len(valid_args) == 0: 
      return f'Hi!' 
   elif len(valid_args) == 1: 
      return f'Hi {valid_args[0]}!'
   else: 
      return f"Hi {', '.join(valid_args[:-1])}, and {valid_args[-1]}!"

#print(hi(name='Mom'))
print(hi('Mom'))
print(hi(''))
print(hi())
hi(None)
print(hi('Mom', 'Dad'))
print(hi('A','B','C'))
print(hi('1', '22', '333', '4444'))


#endregion bailam
