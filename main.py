def organize_list(root_list):
  """
  A exemple of a root_list is:
  root_list = [
      '1 2 10 I',
      '3 1 11 C',
      '1 2 19 R',
      '1 2 21 C',
      '1 1 25 C',
    ]
  Where each line represent a line of the user input.
  The return is a dict, where each key represent the contestant and
  the value is another dict representing the problems. Each key of these
  represent the number of the problem and the value is the solutions entries
  for that problem, for exemple:
  organized_list = {
    '1': {
      '1': [
        {'result': 'C', 'time': '25'}
      ],
      '2': [
        {'result': 'I', 'time': '10'},
        {'result': 'R', 'time': '19'},
        {'result': 'C', 'time': '21'}
      ]
    },
    '3': {
      '1': [
        {'result': 'C', 'time': '11'}
      ]
    }}
  """
  organized_list = {}
  for s in root_list:
    s = s.split(' ')
    contestant = s.pop(0)
    if int(contestant) > 100:
      continue
    problem = s[0]
    if int(problem) > 9:
      continue
    sub_dict = {}
    sub_dict['time'] = s[1]
    sub_dict['result'] = s[2]
    if organized_list.has_key(contestant):
      if organized_list[contestant].has_key(problem):
        organized_list[contestant][problem].append(sub_dict)
      else:
        # First input of a problem
        organized_list[contestant][problem] = []
        organized_list[contestant][problem].append(sub_dict)
    else:
      organized_list[contestant] = {}
      organized_list[contestant][problem] = []
      organized_list[contestant][problem].append(sub_dict)
  return organized_list


def calculate(organized_list):
  """
  Receive a organized_list and return a calculated_dict.
  The calculated_dict calculate the time for the problems, and return the calculated_dict
  where the keys are the contestants and the values are a dict with the number of problems
  solved and the sum of the time it took, plus the 20 minutes for each incorrect answer.
  Example of a calculated_dict:
  calculated_dict = {
    '1': {
      '1': {'still_incorrect': False, 'time': 25},
      '2': {'still_incorrect': False, 'time': 41}
    },
    '3': {
      '1': {'still_incorrect': False, 'time': 11}
    }
  }
   """
  calculated_dict = {}
  for contestant, problems in organized_list.iteritems():
    if not calculated_dict.has_key(contestant):
      calculated_dict[contestant] = {}
    for problem, scores in problems.iteritems():
      for score in scores:
        if not calculated_dict[contestant].has_key(problem):
          if score['result'] == 'I':
            calculated_dict[contestant][problem] = {'time':20,'still_incorrect': True}
          elif score['result'] == 'C':
            calculated_dict[contestant][problem] = {'time':int(score['time']),'still_incorrect': False}
        else:
          if calculated_dict[contestant][problem]['still_incorrect']:
            if score['result'] == 'I':
              calculated_dict[contestant][problem]['time'] += 20
            elif score['result'] == 'C':
              calculated_dict[contestant][problem]['time'] += int(score['time'])
              calculated_dict[contestant][problem]['still_incorrect'] = False
  return calculated_dict


def simplify(calculated_dict):
  """
  Receive a calculated_dict and return a simplify dict.
  The simplify_dict is:
  simplify_dict = {
    '1': {'problems_qty': 2, 'time': 66},
    '3': {'problems_qty': 1, 'time': 11}
    }
  """
  result = {}
  for contestant, problems in calculated_dict.iteritems():
    for problem, score in problems.iteritems():
      if not score['still_incorrect']:
        if not result.has_key(contestant):
          result[contestant] = {}   
        if not result[contestant].has_key('time'):
          result[contestant]['time'] = 0
        if not result[contestant].has_key('problems_qty'):
          result[contestant]['problems_qty'] = 0
        result[contestant]['time'] += score['time']
        result[contestant]['problems_qty'] += 1
  return result


def get_result(root_list):
  """
  Call the others functions to resolve the given list.
  """
  organized_list = organize_list(root_list)
  calculated_dict = calculate(organized_list)
  return simplify(calculated_dict)


if __name__ == "__main__":
  my_list = []
  first_input = raw_input()
  if first_input.isdigit():
    # Read all the entries for scores
    while True:
      line = raw_input()
      if not line:
        break
      my_list.append(line)
    # After read all the scores call get_result to receive the result 
    result = get_result(my_list)
    # With the result ready, print the output
    for contestant, score in result.iteritems():
      print contestant, score['problems_qty'], score['time']
  else:
    print 'You have to start with an integer!'