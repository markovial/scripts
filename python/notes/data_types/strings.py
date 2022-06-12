#https://www.w3schools.com/python/python_ref_string.asp
import textwrap

# DEF Start : split_and_join {{{
def split_and_join():
    sentence = "This is a sentence."
    print(sentence)

    sentence = sentence.split(" ")
    print(sentence)

    sentence = "-".join(sentence)
    print(sentence)

    sentence = sentence.split("-")
    sentence = ",".join(sentence)
    print(sentence)
# }}} DEF End : split_and_join

# DEF Start : case_conversion {{{
def case_conversions():
    string = "abcd 1234 abcd"
    print("lower() : ", string.lower())
    print("upper() : ", string.upper())

    # capitalize() : first character is uppercase
    print("capitalize() : ", string.capitalize())

    # casefold(): Converts string into lower case
    print("casefold() : ", string.casefold())
# }}} DEF End : case_conversion

# DEF Start : check {{{

def check():

    # check if string are alphanumeric (a-z, A-Z and 0-9).
    my_string = "ab123"
    print(my_string.isalnum())

    # checks if all the characters of a string are alphabetical (a-z and A-Z).
    print ("abcD".isalpha())

    # checks if all the characters of a string are digits (0-9).
    print ("1234".isdigit())

    # checks if all the characters of a string are lowercase characters (a-z).
    print ("abcd123#".islower())

    # checks if all the characters of a string are uppercase characters (A-Z).
    print ("ABCD123#".isupper())

    string = "abcd 1234 abcd"
    # string.endswith(value, start, end) 
    # endswith() : check if string ends with specified char / word
    print("endswith() : ", string.endswith("d"))
    print("endswith() : ", string.endswith("abcd"))

# }}} DEF End : check

# DEF Start : align {{{
def align():
    width = 20
    my_string = "text"
    print (my_string.ljust(width,'-'))
    print (my_string.center(width,'-'))
    print (my_string.rjust(width,'-'))

    # textwrap.wrap() : returns a list of lines with given width
    text = "123456789---------"
    text = textwrap.wrap(text, width=9)
    print("textwrap.wrap() : ", text)

    # textwrap.fill() : returns a single string of lines with given width
    text = "123456789---------"
    text = textwrap.fill(text, width=3)
    print("textwrap.fill() :", text)

    # textwrap.shorten() : collapses everything following the first whitespace
    #                      in the string into given width
    text = "123 456 789 0"
    text = textwrap.shorten(text, width=9, placeholder=" ... ")
    print("textwrap.shorten() : ", text)

    # textwrap.indent() : Add prefix to the beginning of selected lines in text.
    text = "123456789"
    text = textwrap.indent(text,'\t')
    print("textwrap.indent() : ", text)

    # textwrap.dedent() : Remove any leading whitespace from every line in text.
    text = "\t123456789"
    text = textwrap.dedent(text)
    print("textwrap.dedent() : ", text)
# }}} DEF End : align

# DEF Start : replace {{{
def change_single_char():
    string = "123456789"
    change_position = 5;

    l = list(string)
    l[change_position] = 'k'
    string = ''.join(l)
    print(string)

    string = "123456789"
    string = string[:change_position] + "k" + string[change_position+1:]
    print(string)

    # str.replace(old, new[, max])

    string = "12121212"
    string = string.replace("1","3")
    print(string)

    string = "12121212"
    string = string.replace("1","3",1)
    print(string)
# }}} DEF End : replace



if __name__ == '__main__':

#    first_name =  input()
#    last_name = input()
#    print (f"Hello {first_name} {last_name}! You just delved into python.")
#    split_and_join()
#    case_conversions()
#    check()
    align()
#    change_single_char()
#    text_wrapping_and_indenting()

    # repr() : returns a printable representation of an object
    string = "abcd 123 abcd"
    string = repr(string)
    print("repr() : " , string)

    # evaluate string as python code
    # eval(x)
    string = "1+1"
    print("eval() : " , eval(string))

    # string = "abcd 1234 abcd"
    # string.count(value, start, end) 
    # count() : returns count of times a item occurs in string
    # print("count() : ", string.count("abcd"))


    # TO ADD :
    # title()
    # find()
    #
    #
    #





