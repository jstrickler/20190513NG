#!/usr/bin/env python

try:
    with open('DATA/chuck_norris.txt') as wombats_in:
        for raw_line in wombats_in:
            print(raw_line.rstrip())
except FileNotFoundError as err:
    print(err)

nums = 5.6, 3.1, 7.9, 0.0, 8.3, 'abc', 6.4

for n in nums:
    try:
        result = 22 / n
    except ZeroDivisionError as err:
        pass
    except (TypeError, ValueError) as err:
        print(err)
    except Exception as err:
        print(err)
    else:  # all good! no errors
        print(result)
    finally:
        pass
