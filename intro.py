# Leetcode

# def findNumber(l, r):
#     a=[]
#     for i in range(l,r+1):
#         if i % 2==1:
#             a.append(i)
#     return a


# print(findNumber(2,7))

# def removeDuplicates(nums):
#     m=0
#     for i in range(len(nums)):
#         n=0
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:n+=1
#         if n > 0: m+=1
#     return len(nums) - m


# print(removeDuplicates([1,1,2]))

# def f(x):
#     def g(y):
#         return y + x + 3
#     return g

# nf1= f(1)
# print(nf1(1))


# def addOperators(num):
#     string=""
#     if strs:
#         shortest = min(len(i) for i in strs)
#         for i in range(shortest):
#             count=0
#             for j in range(1,len(strs)):
#                 if strs[0][i] == strs[j][i]:count+=1
#                 else: return string
#             if count == len(strs) -1 : string+=strs[0][i]
#     return string



# print(addOperators(["flower","flow","flight"]))

# strr=''
# string = "A man, a plan, a canal: Panama"
# strr=''.join(e for e in string if e.isalnum())
# print(strr)

# def isPalindrome(s):
#     z=''.join(e for e in s if e.isalnum())
#     z=z.lower()
#     if z=="" or z==" ":return True
#     rev=z[::-1]
#     return s==rev
    # if len(z)>=1:
    #     count=0
    #     for i in range(len(z)//2 +1):
    #         if z[i] == z[-i-1]:
    #             count+=1
    #         else: return False
    #     if count: return True
    # return False


# print(isPalindrome(""))

# for c in string.punctuation:
#     s = s.replace(c, "")
#     s=s.replace(' ','').lower()
#     rev=s[::-1]

#     return s==rev


# def toGoatLatin(S):
#     strr=S.split(' ')
#     new_str=[]
#     j=1
#     for i in strr:
#         if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' or i[0] == 'A' or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U':
#             new_str.append(i+'ma'+'a'*j)
#         else : new_str.append(i[1:]+i[0] + 'ma'+'a'*j)
#         j+=1
#     return ' '.join(new_str)

# print(toGoatLatin('I speak Goat Latin'))

# def longestPalindrome(s):
#     new_str=''
#     count=0
#     for i in range(len(s)):
#         x=s[:1+count]
#         if x == x[::-1]:
#             print(x,x[::-1])
#             new_str = x
#         count+=1
#     return new_str


# print(longestPalindrome('cbbd'))


# def searchInsert(nums, target):
#     for i,j in enumerate(nums):
#         if j == target:
#             return j
#         if target < j:
#             return i



# print(searchInsert([1,2,3,5,6],4))

# def lengthOfLongestSubstring(s):
#     new_str=''
#     for i in range(len(s)):
#         if s[i] not in new_str:
#             new_str+=s[i]


# print(lengthOfLongestSubstring('pwwkewwww'))

# def myPow(x, n):
#     n_power=1.0
#     for i in xrange(1,abs(n)+1):
#         n_power*=x
#     if n < 0: return 1/n_power
#     else :return n_power


# print(myPow(-2,31))

# def reverseString(s):
#     vowe_in_str=''
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     rev_str= [m for m in s if m in vowels]
#     for i in range(len(s)):
#         if s[i] in vowels:
#             vowe_in_str+=rev_str[-1]
#             rev_str=rev_str[:-1]
#         else: vowe_in_str+=s[i]
#     return vowe_in_str


# print(reverseString('leetcode'))

# def firstUniqChar(s):
#     if len(s) == 1: return 0
#     for i in range(len(s)):
#         if not s[i] or not s[i+1:] : return -1
#         if s[i] not in s[i+1:]:
#             return i
#     return -1


# print(firstUniqChar('aadadaad'))


# def reverseWords(s):
#     m=[]
#     z=s.split(' ')
#     #print(len((z[0])))
#     for i in z[::-1]:
#         if len(i) != 0:
#             m.append(i)
#     return len(' '.join(m))


# print(reverseWords("    "))

# def reverseStr(s, k):
#     return s[:k][::-1]+s[k:]




# print(reverseStr('abcdefg',2))

# def divide(dividend, divisor):
#     count=0
#     i=abs(divisor)
#     while dividend > 0 and i>=0:
#         dividend = dividend - abs(divisor)
#         if dividend > 0:count+=1
#         i-=1

#     if divisor < 0: return -1 * count
#     else :return count

# print(divide(-2147483648,-1))

# def maxProduct(nums):
#     master=[]
#     if len(nums) > 1:
#         for i in range(len(nums)-1):
#             master.append(nums[i]*nums[i+1])

#         return max(master)
#     else : return nums[0]


# print(maxProduct([0,2]))

# board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

# print('E' in board)

# def multiply(num1, num2):
#     count=0
#     for i in range(len(num1)):
#         for j in num2[::-1]:
#             print(i,j)



# print(multiply('123','456'))
# def maxSubArray(nums):
#     max_array=[]
#     sums= nums[0]
#     for i in range(len(nums)):
#         max_array.append(nums[i])
#         print(max_array)
#         print(sums)
#         if sum(max_array) >= sums:
#             sums = sum(max_array)
#             print(sums)
#         else:
#             prev_sum= sums
#             del max_array[0]
#             sums =
#     if prev_sum > sums : return prev_sum
#     else: return sums


# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# def repeatedStringMatch(A, B):
#     a=1
#     orig_a = A
#     while len(B) <= 10000 or len(A) <= 10000:
#         if B in A:
#             print(B,A)
#             return a
#         else:
#             A+=orig_a
#             a+=1
#     return a

# print(repeatedStringMatch('abc','cabcabca'))
# def missingNumber(nums):
#     for i in range(len(nums)+1):
#         if i not in nums:
#             return i
#         continue


# print(missingNumber([0]))

# def findMaxConsecutiveOnes(nums):
#     count,prev_max_count= 0,0
#     if len(nums) <= 10000 and len(nums) >= 1 :
#         prev_count=0
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 count+=1
#             else:
#                 if count >= prev_max_count: prev_max_count = count
#                 count=0
#     return max(count,prev_max_count)


# print(findMaxConsecutiveOnes([1]))

# def rotate(nums, k):
#     for i in range(k):
#         nums = [nums[-1]] + nums[:-1]


# num=[1,2,3,4,5,6,7]
# print(rotate(num, 3))
# print(num)

# def rotatedDigits(N):
#     not_valid=[0,1,8,7,4,3]
#     count=0
#     for i in range(1,N+1):
#         Z=[int(d) for d in str(i)]
#         X=[z for z in Z if z in not_valid]
#         if len(X) <1 : count+=1
#     return count




# print(rotatedDigits(857))

# def detectCapitalUse(word):
#     count=0
#     lower=0
#     if (ord(word[0])) >= 65 and ord(word[0]) <=90 :
#         print(word[0])
#         for i in range(1,len(word[1:])+1):
#             if (ord(word[i])) >= 65 and ord(word[i]) <=90 : count+=1
#             elif (ord(word[i])) >= 97 and ord(word[i]) <=122 : lower+=1
#         return True if count == len(word[1:]) or lower == len(word[1:]) else False
#     else:
#         for i in range(len(word)):
#             if (ord(word[i])) >= 97 and ord(word[i]) <=122 : lower+=1
#             else: return False
#         return True if lower == len(word) else False



# print(detectCapitalUse('google'))

# def repeatedSubstringPattern(s):
#     sub_str=''
#     count=1
#     for i in range(len(s)):
#         sub_str+=s[i]
#         print(sub_str)
#         if sub_str * count == s:



# print(repeatedSubstringPattern('abab'))

# def findMinDifference(timePoints):
#     z=[]
#     for i in timePoints:
#         z.append([t for t in i.split(':')])
#     time1=int(int(z[0][0]) - int(z[1][0]))
#     time2=int(int(z[0][1]) - int(z[1][1]))
#     print(time1 * 60 + time2)


# print(findMinDifference(["23:59","00:00"]))

# def search(alist, item):
#     first = 0
#     last = len(alist)-1

#     while first<=last:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#                 return midpoint
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1
#     return -1

# print(search([1,2,4,5,6],2))

def multiply(num1, num2):
    for i in range(len(num2)-1,0,-1):
        number1=0
        for j in range(len(num1)-1,0,-1):
            print(num1[i],num2[i])
            sum1=0
            carry=0
            z=int(num1[i]) * int(num2[j])
            if z> 10:
                carry= z%10
                sum1= z//10
                print(carry,sum1)
            else:
                carry = z
            number1+=carry
            print(number1)


print(multiply('123','456'))
