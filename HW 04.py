class Car:
    def fast_Change(self, coupler_inlet, max_capacity, current_percent, target_percent):
        self.coupler_inlet = coupler_inlet
        self.max_capacity = max_capacity
        self.current_percent = current_percent
        self.target_percent = target_percent

        dict = {
            self.coupler_inlet == "Tesla": 135,
            self.coupler_inlet == "CSS Type 2" : 175,
            self.coupler_inlet == "CSS Type 1" : 150,
            self.coupler_inlet == "GB/T" : 120,
            self.coupler_inlet == "CHAdeMo" : 400
        }
    ## method
    def percent_diff(self):
        self.percent_diff = self.target_percent - self.current_percent
    
    def target_kw(self):
        Car.percent_diff(self)
        self.target_kw = self.max_capacity * (self.percent_diff/100)
    
    def finish(self):
        Car.target_kw(self)
        finish_time = (self.target_kw/self.coupler_inlet)*60
        return finish_time

A = fast_Change("CHAdeMo",65.7,10,60)
print(A)
