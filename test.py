import csv
import json


class TestClass(object):

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz

    def fizz_buzz(self, digit_1, digit_2):
        for i in range(1, 100):
            if i % digit_1 == 0:
                if i % digit_2 == 0:
                    print 'fizzbuzz!'
                else:
                    print 'fizz!'
            elif i % digit_2 == 0:
                print 'buzz!'
            else:
                print i

    #-------First branch 1st commit-----------    
    def max_min_diff(self, array):
        max = array[0]
        min = array[1]
        for a in array:
            if a > max:
                max = a
            if a < min:
                min = a
        return max - min
    #--------------------------------------

    #-------First branch 2nd commit--------
    def reversal(self, array):
        new_array = list()
        for i in range(len(array),0):
            new_array.append(array[i])
        return new_array
    #--------------------------------------
    
    def json_to_csv(self, json_file_path, outfile_path):
        """Convert a file containing a list of flat JSON objects to a csv.

        What's a DictWriter, you say? Never heard of it!

        """
        with open(json_file_path) as f:
            data = json.load(f)
        with open(outfile_path, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
