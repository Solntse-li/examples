import my_re_new
 
dka = my_re_new.compile("(<name>a|b)?a{1,2}<name>&&")
errors = dka.ErrorsList
print("dka ~ (<name>a|b)?a{1,2}<name>&&")
if dka.isOk:
	print("DKA was built")
	print("string_dka_1 = aaaa&ab&aa&,aaa&, ba s asdasab&a")
	print("result_1 = ", dka.findall("aaaa&ab&aa&,aaa&, ba s asdasab&a"))
else:
	print("DKA wasn't built")
	print("errors = ", dka.ErrorsList)
print("\n\n")


dka1 = my_re_new.compile("a.(bc)?ac{1,3}")
errors = dka1.ErrorsList
print("dka1 ~ a.(bc)?ac{1,3}")
if dka1.isOk:
	print("DKA was built")
	print("string_dka1 = a@acc avbcac aaakaccc")
	print("result_1 = ", dka1.findall("a@acc avbcac aaakaccc"))
else:
	print("DKA wasn't built")
	print("errors = ", dka1.ErrorsList)
print("\n\n")


dka2 = my_re_new.compile("(abc)?(<li>a|(cb))a.<li>")
errors = dka2.ErrorsList
print("dka2 ~ (abc)?(<li>a|(cb))a.<li>")
if dka2.isOk:
	print("DKA was built")
	print("string_dka2_1 = aabdxfabccbala @ abcaajcb")
	print("string_dka2_2 = abckdnsnd askdajnda")
	print("result_1 = ", dka2.findall("abdxfabccbala @ abcaajcb"))
	print("result_2 = ", dka2.findall("abckdnsnd askdajnda"))
else:
	print("DKA wasn't built")
	print("errors = ", dka2.ErrorsList)
print("\n\n")


dka3 = my_re_new.compile("a+1 2 a.(b|c)")
errors = dka3.ErrorsList
print("dka3 ~ a+1 2 a.(b|c)")
if dka3.isOk:
	print("DKA was built")
	print("string_dka3_1 = aaaaa1 2 akc  bcfdaa1 2 a3bghaaa1 2 aec")
	print("string_dka3_2 = aa1 2akaaa1 2 a)cbc=aaaaaaaaa1 2 a5b")
	print("result_1 = ", dka3.findall("aaaaa1 2 akc  bcfdaa1 2 a3bghaaa1 2 aec"))
	print("result_2 = ", dka3.findall("aa1 2akaaa1 2 a)cbc=aaaaaaaaa1 2 a5b"))
else:
	print("DKA wasn't built")
	print("errors = ", dka3.ErrorsList)
print("\n\n")



print("string_dka_2 = 22314aaaa&&-=we,dbab&&aaa@&")
print("result_2 = ", dka.findall("22314aaaa&&-=we,dbab&&aaa@&"))
print("\n\n")

dka4 = my_re_new.compile("((a|b)+abb")
errors = dka4.ErrorsList
print("dka4 ~ ((a|b)+abb")
if dka4.isOk:
	print("DKA was built")
else:
	print("DKA wasn't built")
	print("errors = ", dka4.ErrorsList)
print("\n\n")


dka5 = my_re_new.compile("(abc)?(<li>a|(cb))a.<liz>")
errors = dka5.ErrorsList
print("dka5 ~ (abc)?(<li>a|(cb))a.<liz>")
if dka5.isOk:
	print("DKA was built")
else:
	print("DKA wasn't built")
	print("errors = ", dka5.ErrorsList)
print("\n\n")


dka6 = my_re_new.compile("(a|b)?a{3,2}&|")
errors = dka6.ErrorsList
print("dka6 ~ (a|b)?a{3,2}&|")
if dka6.isOk:
	print("DKA was built")
else:
	print("DKA wasn't built")
	print("errors = ", dka6.ErrorsList)
print("\n\n")


dka7 = my_re_new.compile("(<name>a|b)?a{2,1}(<name>a+b)")
errors = dka7.ErrorsList
print("dka7 ~ (<name>a|b)?a{2,1}(<name>a+b)")
if dka7.isOk:
	print("DKA was built")
else:
	print("DKA wasn't built")
	print("errors = ", dka7.ErrorsList)
print("\n\n")



dka8 = my_re_new.compile("a.(bc)?ac}")
errors = dka8.ErrorsList
print("dka8 ~ a.(bc)?ac}")
if dka8.isOk:
	print("DKA was built")
else:
	print("DKA wasn't built")
	print("errors = ", dka8.ErrorsList)
print("\n\n")
























