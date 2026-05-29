from database.schemas.base_schema import BaseSchema

class CarSchema(BaseSchema):
    brand: str
    name: str
    bodyType: str
    color: str
    fuelType: str
    year: int
    mileage: int
    transmission: str
    power: int
    price: int
    engineDisplacement: float
    location: str