#!/usr/bin/env python
# encoding: utf-8

class Read():
	def __init__(self,num) :
		self.num = int(num)
		self.sumup = 0

	def sum_up(self) :
		while self.num>0:
			self.sumup += self.num % 10
			self.num //=10
		print('各位数之和为:\n%s' % self.sumup)

	def print_it(self) :
		print('拼音为:')
		list = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
		strA = str(self.sumup)
		a = strA[::-1]
		b = int(a)
		while b > 0:
			index = b % 10
			print(list[index],end = ' ')
			b //= 10

	def change(self) :
		c = self.sumup
		x = int(c)
		symbol = ''
		ans = ''
		while(x):
			ans = str(x%7) + ans
			x = x//7
		print('\n转化为7进制是:\n%s' % symbol+ans)

if __name__ == '__main__' :
	number = Read(input("输入一个尽可能长的数字\n"))
	number.sum_up()
	number.print_it()
	number.change()