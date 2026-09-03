#String reverse karo
#output
#original string:puja
#reversed string:ajup
text='puja'
reverse_text = text[::-1]
print("original string:",text)
print("Reversed string:", reverse_text)
#explanation
#[::-1] slicing ka use hota hai string ko reverse karne ke liye
#-1 ka matlb hai last se start karke ulta print karo



#example2--> count vowels in string
#output
#total vowels=5
text='puja kumari'
vowels="aeiouAEIOU"
count=0
for ch in text:
    if ch in vowels:
        count+=1
print("total vowels:",count)
#explanation





#example3--. palindrome check
text='madam'
if text==text[::-1]:
    print("palindrome")
else:
    print("not palindrome")
#exaplantion
#jo word ulta sidha same ho eg-- madam,level
#if text==text[::-1]:
#ye sabse  important line hai
#text[::-1]kya karta hai?
#[::-1] string ko reverse (ulta) kar deta hai
#"madam" ka reverse bhi "madam" hi hota hai
#ab condition kya check kar rhi hai?
#ye check kar rhi hi"
#original string== Reverse string?
#matlb:
#"madam"=="madam"
#line3 , print("palindrome")
#kynki condition true hai,ye line print hogi , isliye output palindrome

#example2
text=input("enter a number:")
if text==text[::-1]:
    print("palindrome")
else:
    print("Not palindrome")