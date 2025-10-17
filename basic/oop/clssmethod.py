class Iphone:
    def __init__(self,model,btry,year,version):
        self.model =model
        self.btry = btry
        self.year=year
        self.version=version
    
    def display_info(self):
        return f'your {self.model} battery helth is {self.btry}. this model release year is {self.year}.and your phone last updated version {self.version}.'
    

ph1=Iphone("iphone 13 series","85%","2021","ios 18.3.1")
ph2=Iphone("iphone 14 series","95%","2022","ios 18.3.1")
ph3=Iphone("iphone 15 series","98%","2023","ios 26.1.1")
ph4=Iphone("iphone 16 series","100%","2024","ios 26.1.1")
ph5=Iphone("iphone 17 series","100%","2025","ios 26.1.1")

print(ph1.display_info())
print(type(ph1))

