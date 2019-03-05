#Create an apartment object
class Apartment
	attr_accessor :bedrooms, :bathrooms, :price, :city, :utilities
end

apartment_1 = Apartment.new
apartment_1.bedrooms = 3
apartment_1.bathrooms = 1
apartment_1.price = 2039
apartment_1.city = "Paris"
apartment_1.utilities = ["dish washer", "parking", "washing machine"]

apartment_2 = Apartment.new
apartment_2.bedrooms = 5
apartment_2.bathrooms = 2
apartment_2.price = 8293
apartment_2.city = "New York"
apartment_2.utilities = ["dish washer", "parking", "pool", "sauna", "gym"]