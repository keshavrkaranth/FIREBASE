# s = 'aWESOME is cODING'
# k = s.split()
# res = ''
# for i in range(len(k),0,-1):
#     print(i)
#     res +=k[(i-1)].swapcase()+" "
#
#
# print(res)
# print(k)
def reverse_words_order_and_swap_cases(sentence):
    sentence_list = sentence.split()
    resultent_string = ""
    for i in range(len(sentence_list),0,-1):
        resultent_string +=sentence_list[(i-1)].swapcase()+" "
    return resultent_string

print(reverse_words_order_and_swap_cases('aWESOME is cODING'))