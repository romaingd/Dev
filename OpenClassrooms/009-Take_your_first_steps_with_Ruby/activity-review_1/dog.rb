class Dog
	attr_accessor :name, :age, :breed, :color

	def dog_years
		puts @name + " is actually " + (@age*7).to_s + " in dog years!"
	end
end

dog_1 = Dog.new
dog_1.name = "Kuki"
dog_1.age = 2
dog_1.breed = "Labrador"
dog_1.color = ["black","white"]

print dog_1.dog_years