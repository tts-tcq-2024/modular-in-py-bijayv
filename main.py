from color_code import test_number_to_pair
from color_code import test_pair_to_number
from color_code import color_pair_to_string
  
if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print(color_pair_to_string('Violet','Orange'))
  print(color_pair_to_string('Red','Slate'))
  print('Done :)')
