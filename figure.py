import math	# math 모듈의 PI, sqrt 사용을 위해 모듈 불러오기

class Line:
	def __init__(self, len = 1):
		"""__length의 값을 설정합니다.
		값이 양의 실수가 아니거나 값을 제시하지 않으면 1로 설정합니다.
		Args:
			len (int or float) : 설정할 값
		Returns:
		
		"""
		if type(len) != int and type(len) != float or len <= 0:
			len = 1
		self.__length = len
	def set_length(self, len):
		"""__length의 값을 변경합니다.
		값이 양의 실수가 아니면 변경하지 않습니다.
		Args:
			len (int or float) : 변경할 값
		Returns:
		
		"""
		if (type(len) == int or type(len) == float) and len > 0:
			self.__length = len
	def get_length(self):
		"""__length의 값을 반환합니다.
		Args:
		
		Returns:
			int or float : __length를 반환합니다.
		"""
		return self.__length

def area_square(len):
	"""길이를 입력받아 정사각형의 넓이를 반환하는 함수입니다.
		Args:
			len (Line) : 한 변의 길이입니다.
		Returns:
			int or float : 정사각형의 넓이를 반환합니다.
	"""
	if type(len)!=Line:
		return 0
	return pow(len.get_length(),2)

def area_circle(len):
	"""길이를 입력받아 원의 넓이를 반환하는 함수입니다.
	Args:
		len (Line) : 반지름의 길이입니다.
	Returns:
		int or float : 원의 넓이를 반환합니다.
	"""
	if type(len)!=Line:
		return 0
	return pow(len.get_length(),2)*math.pi

def area_regular_triangle(len):
	"""길이를 입력받아 정삼각형의 넓이를 반환하는 함수입니다.
	Args:
		len (Line) : 한 변의 길이입니다.
	Returns:
		int or float : 정삼각형의 넓이를 반환합니다.
	"""
	if type(len)!=Line:
		return 0
	return pow(len.get_length(),2)*math.sqrt(3)/4

