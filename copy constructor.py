class Mobile:
    def __init__(self,brand,model,price,RAM):
        self.brand=-brand
        self.model=model
        self.price=price
        self.RAM=RAM

        @classmethod
        def __copy(cls,other):
            return cls(other.brand,other.model,other.price,other.RAM)
        
        M1=Mobile()
        M1.brand="Google Pixel"
        M1.model="pixel6"
        M1.price="Rs 30,000"
        M1.RAM="8GB"

        M2=Mobile.copy()
        print("M2 copy of M1",M2.brand,M2.price)


        
                 