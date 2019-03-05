class Course
    attr_accessor :title, :chapters, :nb_followers

    def describe
        print "This course is entitled '#{@title}', and consists in the following chapters: #{@chapters}.\n"
        print "It is currently followed by #{@nb_followers} followers.\n"
    end

    def add_followers(nb_new_followers)
        @nb_followers += nb_new_followers
    end

    def remove_followers(nb_quitting_followers)
        @nb_followers -= nb_quitting_followers
    end
end


# ruby_course = Course.new
# ruby_course.title = "Take your first steps with ruby"
# ruby_course.chapters = ["Fundamental Ruby concepts", "Dive into Ruby data types"]
# ruby_course.nb_followers = 5

# ruby_course.add_followers(10)
# ruby_course.describe()