import unittest

#if weight is obese(greater than or equal to 80)
def check(num):
	return num>=80

class checkFunction(unittest.TestCase):

	def test(self):
		self.assertTrue(check(80))

#area of the rectangle
def test_rectangle_area():
    lenght = 5
    width = 5
    area = ((lenght + width)*2)
    assert area == 20
	
# temperature from kelvin to fahrenheit
    kelvin = 318.2
    fahrenheit = ((kelvin - 273.15) * (9/5) + 32)
    assert fahrenheit == 77.05000000000001


if __name__ == "__main__":
    unittest.main()