import re

#EX1
arr = ['fruits', 'flower', 'vegetables', 'apple', 'banana']

#a/ Print length,  the first and last element of  array
print("Length of array: ",len(arr), "\n")
print("The first and last element: ",arr[0], arr[-1], "\n")

#b/ Print all elements of array
for x in arr:
    print(x)
print()

#c/ Verify if any element in array contains 'tables'



#EX2
#Dict
myDict = {'a':1, 'b':2, 'c':3}

#a/ Print all key of dict and then add them into an array
keyDict = list(myDict.keys())
print("Key of array: ", keyDict, "\n")

#b/ Print key/value of dict
print("Key/Value of dict:")
for key, value in myDict.items():
    print(key, '-', value)

#c/ Check if a key is exist.
check_key = 'b'
if check_key in myDict:
    print("Key", check_key, "is exist.")
else:
    print("Key", check_key, "is not exist")

#d/ Print size of dict
print("Length of Dictionary:", len(myDict),"\n")


#EX3
#String
given_string = "A regular expression (abbreviated regexp or regex) is a way to describe sets of characters using syntactic rules. Many programming languages use or support regular expression. A REGULAR expression is then used by a special program or part of a programming language."

#a/ Verify if string contains 'Perl'
check_string = 'Perl'
if check_string in given_string:
    print("The string contains 'Perl'.")
else:
    print("The string does not contains 'Perl'.")
    
#b/ Replace all “regular/REGULAR expression” with “PERL”.
replace_string = re.sub(r'regular|REGULAR expression', 'PERL', given_string)
print(replace_string, "\n")

#EX5

# Given array
arr = ['<IPDR xsi:type="test">',
       '<VoIP:uniqueCallId>005c-0100-2034-ffffffff@h10-250-191-194</VoIP:uniqueCallId>',
       '<VoIP:callProgressState>5</VoIP:callProgressState>',
       '<nortel:recordID>f37f9294a6157fb0073e58013bcaa52912532e5a9</nortel:recordID>',
       '<nortel:recTime>2019-04-23T07:47:28.191Z</nortel:recTime>',
       '<nortel:ansInd>true</nortel:ansInd>',
       '</IPDR>']

#a/ Count number of lines that contain 'VoIP' or 'Nortel'. 
count = 0
for line in arr:
    if 'VoIP' in line or 'nortel' in line:
        count+=1
print ("a/ Result after count: ",count, "\n")
"""
count = sum(1 for line in arr if 'VoIP' in line or 'nortel' in  line)
print("a/ Result after count:", count)
"""

#b/ Print out value of 'uniqueCallId'.3
for line in arr:
    if 'VoIP:uniqueCallId' in line:
        value_call_id = re.search(r'<VoIP:uniqueCallId>(.*?)@h10-250-191-194</VoIP:uniqueCallId>', line)
print("b/ Value of uniqueCallId:",value_call_id.group(1), "\n")

#c/ Print out value of 'recordID'
for line in arr:
    if 'recordID' in line:
        value_record_ID = re.search(r'<nortel:recordID>(.*)</nortel:recordID>', line)
print("c/ Value of recordID: ",value_record_ID.group(1), "\n")

#d/ Print out value of month in 'recTime' line
for line in arr:
    if 'nortel:recTime' in line:
        value_of_month = re.search(r'<nortel:recTime>(.*?)T', line)
print("d/ Value of month in recTime: ",value_of_month.group(1))



#EX6
employee = {
    'em1': {
        'name': 'A',
        'year': 10
        },
    'em2': {
        'name': 'B',
        'year': 15
    }
}

#a/ Print info of em1, em2 (name and year)
for x, obj in employee.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])
print("\n")
        
#b/ Print year of em2. (Result: 15)
print("Year off em2:" ,employee["em2"]["year"])

#EX7
# Given array
number = ['Total 5136',
          '1-113-VOIPMGCTRUNKGROUP',
          '1-1500-VOIPMGCTRUNKGROUP',
          '1-5067-VOIPMGCTRUNKGROUP',
          '1-VOIPMGSUBTRUNKGROUP',
          '2-12-VOIPMGCTRUNKGROUP']

#a/ Print value of total
total = number[0].split()[1]
print("Value of total: ",total)

#b/ Add value of VOIPMGCTRUNKGROUP into a array and print out that array. 
number.append("1-1-VOIPMGCTRUNKGROUP")
print(number)


#EX9
# Given string
string = "I'm always happy and excited when newyear comes since this is the time when I come back my hometown. Seeing everyone in my family gets me feeling so good"

# Transforming the string into an array of words
array = string.split()
print("a/: ",array, "\n")

# Printing 2nd, 6th, and 20th elements
print("b/: ",array[1], array[5], array[19])


#EX10
#create dictionary

student1 = {
  "name" : "Lucy",
  "age" : 20
}
student2 = {
  "name" : "Jamie",
  "age" : 18
}

mystudent = {
  "student1" : student1,
  "student2" : student2
}

#a/ Printing out the names and the ages of the two students
print("a/")
for x, obj in mystudent.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])
print("\n")


#b/ Add another key-value as id-1111 to hash student1
student1["id"] = "1111"
print("b/\nstudent1:" ,student1)


#EX11
msgIn = {
    '-pattern': {
        'Cat': {
            '1': [
                'SGW_SIP_ID', 'CP_CALLM_ID',
                'ID_CHANNEL_ID SIP_DAL 20100',
                'ID_CALLED_PARTY_NUM 1300000000',
                'ID_CALLING_PARTY_CAT CGPCAT_PAY_PHONE'
            ]
        }
    },
    '-tcid': "TC_01",
    '-start_boundary': 'ECCP_CC_SETUP'
}

#a/ Print out "ID_CALLING_PARTY_CAT CGPCAT_PAY_PHONE" in this dict.
print("Value: ", msgIn['-pattern']['Cat']['1'][4])

#b/ Delete key "-tcid" and then print out the dict.
del msgIn['-tcid']
print("Dictionary after delete '-tcid'",msgIn)


# Given array
number = ['Total 5136',
          '1-113-VOIPMGCTRUNKGROUP',
          '1-1500-VOIPMGCTRUNKGROUP',
          '1-5067-VOIPMGCTRUNKGROUP',
          '1-VOIPMGSUBTRUNKGROUP',
          '2-12-VOIPMGCTRUNKGROUP']

# a/ Print value of total
total = int(number[0].split()[1])
print("a/ Print value of total:", total)

# b/ Add value of VOIPMGCTRUNKGROUP into an array and print out that array
voip_trunk_groups = [line.split('-')[-1] for line in number[1:] if 'VOIPMGCTRUNKGROUP' in line]
print("b/ Array of VOIPMGCTRUNKGROUP:", voip_trunk_groups)

