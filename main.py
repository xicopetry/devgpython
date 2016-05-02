#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The python test!

This is a simple riddle discrebe like a sccore board for ACM ICPC!

The score board Judge goona put the Inputs that the contest did in that order:

    integer -This initialize the program
    InputComponent -> This is a namedtuple with the values of:
        -> Name of the Contestant;
        -> The identification of the problem that was tried to do;
        -> The time that was tooked to do the Problem;
        -> And the result.

    So, each Contestant is doing a bunch of problems each one by time.
    Each Contestant can have a many Problems.
    A Problem have a (name), (time) and a (result).

    A Problem is considered solved by a contestant if any of the submissions
    for that problem was judged correct. Penalty time is computed as the the
    number of minutes it took until the first correct submission for a problem
    was received, plus 20 minutes for each incorrect submission prior to the
    correct solution.

"""

from collections import defaultdict
from collections import namedtuple
from itertools import groupby
from operator import attrgetter
import sys


def get_contestants():

    user_inputs = []
    while True:
        line = raw_input()
        # import ipdb; ipdb.set_trace()
        if not line:
            break
        user_inputs.append(line)
    # Discart all the inputs that dont matter, and save the order
    user_inputs = filter_inputs(user_inputs)
    contestants = []
    # Divide all the Inputs in problems per Contestant
    for (contestant, inputs) in groupby(user_inputs, lambda x: x.contestant):
        problems = []
        for (problem_name, results) in groupby(inputs, lambda x: x.problem):
            problems.append(Problem(name=problem_name, results=results))
        contestants.append(Contestant(name=contestant, problems=problems))

    return contestants


def filter_inputs(user_inputs):
    """
    Attributes:
        user_inputs = List of the inputs
    This is a filter of valid inputs.
    Receive a list of inputs and will return only valid values of this.
    The return is a namedtuple of a Input.
    """

    inputs = []
    for (index, user_input) in enumerate(user_inputs):
        user_input = user_input.split(' ')
        # Rule 1 - The input must have four arguments:
        # Contestant, Problem, Time and the Result
        if len(user_input) != 4:
            continue
        # Rule 2 - The contestant must be a number between 1 to 10
        if not user_input[0].isdigit() or not int(user_input[0]) in range(1, 10):
            continue
        # Rule 3 - The problem must be a number between 1 to 100
        if not user_input[1].isdigit() or not int(user_input[1]) in range(1, 100):
            continue
        # Rule 4 - The time must be just a number
        if not user_input[2].isdigit():
            continue
        # Rule 5 - Will discart all the entries for results diferent then C or I
        if not user_input[3] in ['C', 'I']:
            continue
        # The input that pass all the rules it is a valid Input
        inputs.append(
            namedtuple(
                'Input',
                'contestant, problem, time, letter index'
            )._make(
                (
                    int(user_input[0]),
                    int(user_input[1]),
                    int(user_input[2]), user_input[3],
                    index
                )
            )
        )
    return sorted(inputs, key=attrgetter('contestant', 'index'))


class Contestant:

    def __init__(self, name, problems=[]):
        """
        Attributes:
            name = Int representing the name of the Contestant
            contestant_problems = List of the Problems dided by the Contestant
        """
        self.name = name
        self.problems = problems
        self.quantity_problems = 0
        self.total_time = sum(self.problems)
        for problem in self.problems:
            if problem.solved:
                self.quantity_problems += 1

    def __repr__(self):
        return '%s %s %s' % (self.name, self.quantity_problems, self.total_time)


class Problem:

    def __init__(self, name, results=[]):
        """
        Attributes:
            name = Int representing the name of the Problem
            results = List of the Inputs with the same Problem
        """
        self.results = sorted(results, key=attrgetter('index'))
        self.name = name
        self.time = 0
        self.solved = False
        self.calculate_time()

    def calculate_time(self):
        """
        This method will calculate the total time that the problem tooked to be
        solved. Will sum the 20 of penalty for all the incorrect Inputs until
        find a correct result.
        """
        for result in self.results:
            if not self.solved:
                if result.letter == 'C':
                    self.solved = True
                    self.time += result.time
                    break
                if result.letter == 'I':
                    if result.time > 20:
                        self.time += result.time
                    else:
                        self.time += 20

    def __radd__(self, other):
        """
        Method used to guide the class to do the sum(Problems).
        If the problem is not solved, it does not represent penalty.
        """
        if self.solved:
            return other + self.time
        else:
            return other


def main():
    """
    This is the main function of the sistem. Ok, not acctualy the main, but
    it is the caller of the rest of all others.
    """
    print_return = []
    while True:
        first_input = raw_input()
        if first_input.isdigit():
            contestants = get_contestants()
            for contestant in contestants:
                print_return.append(contestant.__repr__())
        else:
            print 'You need to start with an integer!'
        break
    return print_return


if __name__ == '__main__':
    print 'Welcome to the Contest Scoreboard!'
    print 'Write down the snapshot of judging queue:'
    print_return = main()
    for contestant in print_return:
        print contestant