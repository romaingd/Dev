# Playing with objects
class Person
    attr_accessor :name, :age, :outfit

    def say_hello
        @name + " says hello!"
    end

    def say_goodbye
        @name + " says goodbye!"
    end
end

person_1 = Person.new
person_1.name = "Arnaud"
person_1.age = 32
person_1.outfit = ["blue top", "red pants", "white shoes"]

person_2 = Person.new
person_2.name = "Emma"
person_2.age = 34
person_2.outfit = ["red sweater", "white pants", "white shoes"]

print person_1.say_hello + "\n"
print person_1.say_goodbye + "\n"

print "Update your profile, #{person_1.name}" + "\n"
print "\n"


# Playing with strings
print "The sentence 'I ate it' has #{'I ate it'.length} characters\n"
print "The sentence 'I ate it' has #{'I ate it'.count('t')} 't' characters\n"
print "\n"

print "The sentence 'I ate it' can be uppercased: '#{'I ate it'.upcase}'\n"
print "The sentence 'I ate it' can be lowercased: '#{'I ate it'.downcase}'\n"
print "\n"

sentence = "I ate it"
print "Original sentence: '#{sentence}'\n"
sentence.upcase!
print "Uppercased bang sentence '#{sentence}'\n"
print "\n"


# Playing with numbers
print "17/9: #{17/9}\n"
print "17.0/9.0: #{17.0/9.0}\n"
print "\n"

def check_password(password)
    if password.length > 20
        puts "Your password is good!\n"
    else
        puts "Your password is not long enough.\n"
    end
end

print check_password("dog")
print check_password("mlfjsflkhsfmuhgamebksdbfkjfgdkfjbs,fbds")
print "\n"


# Playing with arrays
foods = ["olive oil", "almonds", "apples"]
foods[3] = "strawberries"
foods.push("celery", "ketchup")
foods << "whole wheat meat"
foods.unshift("birthday cake")
print foods
print "\n"


# Playing with hashes
favorites = {
    books: ["Paris guidebook", "The Art of Innovation"],
    fruits: ["apples", "oranges", "pears"],
    colors: ["yellow", "green"]
}
print favorites[:books], "\n"