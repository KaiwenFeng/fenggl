
import os
class Dog:
	"""测试狗类"""
	
	def __init__(self, name, age):
		"""初始化类形参"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟狗狗被命令坐下"""
		print(self.name.title() + " is now sitting. ")
		
	def roll_over(self):
		"""模拟狗狗命令被打滚"""
		print(self.name.title() + " is now roll over. ")
		
animal = Dog('kk','18')
animal.sit()
animal.roll_over()

num = [1, 2, 3, 4, 5]

print([chr(i) for i in range(65, 91)])```