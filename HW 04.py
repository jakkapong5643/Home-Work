def fast_charge(self, coupler_inlet, max_capacity, current_percent, target_percent):

    dict = {
        "Tesla" : A == 135,
        "CSS Type 2" : A == 175,
        "CSS Type 1" : A ==150,
        "GB/T" : A == 120,
        "CHAdeMo" : A == 400
    }
    ## method
    def Method():
        percent_diff = round((target_percent - current_percent))
        target_kw = round((max_capacity * (percent_diff /100)))
        finish_time = round(((target_kw / A) * 60))
        return finish_time
a = fast_Change("CSS Type 2",65.7,10,60)
print(a)
    
