class PraiseMusic
  attr_accessor :singer, :bandName, :releaseYear, :gender, :topHits

  def praise
    puts @singer + " from " + @bandName + " sang: Praise the Lord! "
  end
end

artist_1 = PraiseMusic.new
artist_1.singer = "Kari Jobe"
artist_1.bandName = "KariJobe"
artist_1.releaseYear = 2009
artist_1.gender = "Female"
artist_1.topHits = ["Lord over All", "I am not alone", "Let your glory fall"]
