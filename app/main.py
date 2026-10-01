import datetime


class NotWearingMaskError(Exception):
    pass


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name


    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        
        visitor_vaccine = visitor["vaccine"]
            
        if visitor_vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError
        
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"