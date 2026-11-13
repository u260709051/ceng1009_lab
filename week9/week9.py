def is_odd(n):
    if n%2==1:
        return True
    return False
#print(is_odd(13))

def is_leapyear(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

#print(is_leapyear(2100))



def print_triangular_numbers(n):
    total=0
    for i in range(1,n+1):
        total+=i
        print(i,total)

#print_triangular_numbers(5)

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True

#print(is_prime(5))

def reverse(s):
    result=""
    for ch in s:
        result=ch+result
    return result

#print(reverse("hello world"))

def reverse_slice(s):
    return s[::-1]


#print(reverse_slice("hello world"))


def remove_all_occurances(sub,s):
    return s.replace(sub,"")
#print(remove_all_occurances("l","hello world"))
#print(remove_all_occurances("a","banana"))



def substitude(message,key):
    alphabet="abcçdefgğhıijklmnoöprsştuüvyz"
    result=""
    for ch in message:
        index=alphabet.find(ch.lower())
        if index ==-1:
            result=result+ch
        elif ch.isupper():
            result = result+key[index].upper()
        else:
            result=result+key[index].lower()
    return result

key="qtgasdfhjklşizxcvbnmweryuıopz"

#print(substitude("hello world",key))

def remove_dubs(s):
    result=""
    for ch in s:
        if ch.lower() not in result.lower():
            result=result+ch
    return result

print(remove_dubs("hello world"))
print(remove_dubs("heLlo world"))
print(remove_dubs("banana"))