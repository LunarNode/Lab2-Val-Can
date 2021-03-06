from ..NumGen import num_generator

class Pentagon(num_generator):
    def __init__(self):
        self.name = "Pentagon Series"
        self.series = []
        super().__init__(self.name)
        
        

    def finite_series(self):
        self.get_range()
        self.list_n = list(range(self.lower_bound, self.upper_bound + 1))
        self.series = [ int(3*n*(n-1)/2 + n) for n in self.list_n]
        self.n = len(self.list_n)
        self.display(self.name, self.series, len(self.list_n))

    def infinite_series(self):
        self.n = int(input("enter the number of values :"))
        self.series = [ int(3*i*(i-1)/2 + i) for i in range(1, self.n + 1)]
        self.display(self.name, self.series, self.n)

    def mean(self):
        if len(self.series) != 0:
            avg = num_generator.get_mean(self.series)
            print("mean of series is :", avg)
        else:
            print("Missing Data please choose following:")
            flag = int(input("Enter 1 for finite and any other key for infinite series "))
            if flag == 1:
                self.finite_series()
            else:
                self.infinite_series()

    def Median(self):
        if len(self.series) != 0:
            self.median = num_generator.get_median(self.series)
            print("median of series:", self.median)
        else:
            print("Missing Data please choose following:")
            flag = int(input("Enter 1 for finite and any other key for infinite series "))
            if flag == 1:
                self.finite_series()
            else:
                self.infinite_series()