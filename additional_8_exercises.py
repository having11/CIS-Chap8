import string

#1: rainfall totals
rainfall_totals = []
def get_rainfall(month_num):
    rainfall_entered = float(input("Enter the rainfall for month {0}:\n".format(month_num)))
    rainfall_totals.append(rainfall_entered)

def display_totals():
    total_rainfall = sum(rainfall_totals)
    
    print("Total rainfall: %.2f\naverage rainfall: %.2f\nhighest rainfall month: %d\n \
lowest rainfall month: %d" % (total_rainfall,total_rainfall/12,rainfall_totals.index(max(rainfall_totals)),
                                  rainfall_totals.index(min(rainfall_totals))))

for i in range(12):
    get_rainfall(i)
display_totals()
                                  
#2: custom list program

view_counts = []
view_counts.append(30000)
view_counts.append(24003)
print("Most views:",max(view_counts))
print("Least views:",min(view_counts))

#3: coded messages
lowercase_chars = list(string.ascii_lowercase)
codes = {}
for index, char in enumerate(lowercase_chars):
    codes[char] = chr((index*2)+33)
    codes[char.upper()] = chr((index*2)+34)
codes[' '] = ' '
def decode_sentence(sentence):
    sentence_decoded = ""
    for search_char in sentence:
        for char, encoded_char in codes.items():
            if encoded_char == search_char:
                sentence_decoded += char
    print("Decoded sentence:",sentence_decoded)

def input_sentence():
    sentence = input("Enter a sentence to encode:\n")
    new_sentence = ""
    for char in sentence:
        new_sentence += codes[char]
    print("Encoded sentence:",new_sentence)
    decode_sentence(new_sentence)

input_sentence()

#4: custom dictionary program
    
student_scores = {"Bill": [12.5,100],"Randy": [34,70],"Susan": [55,94]}
print(student_scores)
del student_scores["Randy"]
print("Bill's average score:",sum(student_scores["Bill"])/2)

