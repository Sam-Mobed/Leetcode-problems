"""
Just to test stuff.
"""

def merge(intervals):

    intervals.sort(key= lambda i : i[0])

    new_intervals = [intervals[0]]

    for first,last in intervals[1:]:
        if first<=new_intervals[-1][1]:
            if new_intervals[-1][1]<last:
                new_intervals[-1][1]=last
        else:
            new_intervals.append([first,last])

    return new_intervals

merge([[1,3],[4,8],[1,10]])