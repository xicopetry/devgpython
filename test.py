import main

# Test file

# File with all the tests of the system



class MainTest():
  """
  Main class to manage the tests
  """

  def execute(self):
    """
    Method that execute the tests
    """
    self.test_get_result_exercise_example()
    self.test_get_result_empty_list()
    self.test_get_result_all_correct()
    self.test_get_result_not_allowed_problem()
    self.test_get_result_not_allowed_contestant()

  def test_get_result_exercise_example(self):
    """
    Test that use the same input as the exercise example
    """
    test_list = [
      '1 2 10 I',
      '3 1 11 C',
      '1 2 19 R',
      '1 2 21 C',
      '1 1 25 C',
    ]
    result = main.get_result(test_list)
    expected_result = {
      '1': {'problems_qty': 2, 'time': 66},
      '3': {'problems_qty': 1, 'time': 11}
    }
    if result == expected_result:
      print "test_get_result_exercise_example - ok"  
    else:
      print "test_get_result_exercise_example - error"

  def test_get_result_empty_list(self):
    """
    Test if the return of a empty input its correct managed
    """
    test_list = []
    result = main.get_result(test_list)
    expected_result = {}
    if result == expected_result:
      print "test_get_result_empty_list - ok"  
    else:
      print "test_get_result_empty_list - error"
  
  def test_get_result_all_correct(self):
    """
    Test that use a input with all corrects
    """
    test_list = [
      '1 2 15 C',
      '3 1 11 C',
      '1 1 5 C',
      '1 3 20 C',
      '1 4 25 C',
    ]
    result = main.get_result(test_list)
    expected_result = {
      '1': {'problems_qty': 4, 'time': 65},
      '3': {'problems_qty': 1, 'time': 11}
    }
    if result == expected_result:
      print "test_get_result_all_correct - ok"  
    else:
      print "test_get_result_all_correct - error"

  def test_get_result_not_allowed_problem(self):
    """
    Test that use a input with a problem greater than 9.
    According to exercise it should not allow problems greater than 9.
    """
    test_list = [
      '1 10 15 C',
      '3 1 11 C',
    ]
    result = main.get_result(test_list)
    expected_result = {
      '3': {'problems_qty': 1, 'time': 11}
    }
    if result == expected_result:
      print "test_get_result_not_allowed_problem - ok"  
    else:
      print "test_get_result_not_allowed_problem - error"

  def test_get_result_not_allowed_contestant(self):
    """
    Test that use a input with a contestant greater than 100.
    According to exercise it should not allow contestant greater than 100.
    """
    test_list = [
      '101 1 15 C',
      '3 1 11 C',
    ]
    result = main.get_result(test_list)
    expected_result = {
      '3': {'problems_qty': 1, 'time': 11}
    }
    if result == expected_result:
      print "test_get_result_not_allowed_contestant - ok"  
    else:
      print "test_get_result_not_allowed_contestant - error"

if __name__ == "__main__":
  test = MainTest()
  test.execute()