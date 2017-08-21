m = int(input('please input the orinal number system'))
n = int(input('please input objective number system'))
m_str = input('the orginal integer')

if(float(m_str)==int(float(m_str))):
	m_number = int(m_str,m)
	symbol = ''

	if(m_number<0):
		m_number = abs(m_number)
		symbol = '-'

	if(n == 10):
		print(symbol+str(m_number))
	else:
		ans = ''
		while(m_number):
			ans = str(m_number%n) + ans
			m_number = m_number//n
		print(symbol+ans)
else:
	print('input is not integer')