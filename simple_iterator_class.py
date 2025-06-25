class Months:
    MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    def __init__(self):
        self._index = -1

    def __iter__(self):
        return self  # must return object implenting __next__
    
    def __next__(self):
        self._index += 1
        if self._index > (len(self.MONTHS) - 1):
            raise StopIteration()
        else:
            return self.MONTHS[self._index]

if __name__ == "__main__":
    m = Months()
    month = next(m)
    print("first:", month)
    for month in m:
        print(month)