#coding:utf-8
import ex17_more_more_execise as ex17

sentence = "All good things come to those who wait."
print "Print original sentence : %s" %sentence

# 分割sentence，并返回副本
"""['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']"""
words = ex17.break_words(sentence)
print "After splited, words = %r" %words
print "After splited, sentence = %r" %sentence

# 将words排序后返回
"""['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']"""
sorted_words = ex17.sort_words(words)
print "After sorted, sorted words = %r" %sorted_words

# 打印首个单词，并剔除之
ex17.print_first_word(words)
# 打印最后一个打次，并剔除之
ex17.print_last_word(words)
# 打印剔除之后的words
"""['good', 'things', 'come', 'to', 'those', 'who']"""
print "After poped, words = %r" %words

ex17.print_first_word(sorted_words)
ex17.print_last_word(sorted_words)
print "After poped, sorted_words = %r" %sorted_words

ex17.print_first_and_last(sentence)

ex17.print_first_and_last_sorted(sentence)
