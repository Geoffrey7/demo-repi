class PhoneNumber:
    @staticmethod
    def fromat_kenyan_phone_number(phone_number: str) -> str:
        # Removes all white spaces in the phone number

        phone_number = phone_number.strip()

        if phone_number.startswith("+254"):
            return phone_number
        
        if phone_number.startswith("0"):
            phone_number = "+254" + phone_number[1:] #start from index 1
        else:
            phone_number = "+254" + phone_number

        return phone_number

print(PhoneNumber.fromat_kenyan_phone_number("0727505564"))     

        
        
        
        
