class Post < ApplicationRecord
  belongs_to :user

  validates :title, presence: true
  validates :body, presence: true

  has_attached_file :photo, styles: { medium: "300x300", thumb: "100x100"}, default_url: ".images/:style/missing.png"
  validates_attachment_content_type :photo, content_type: /\Aimage\/.*\z/

  geocoded_by :address
  after_validation :geocode, :if => :address_changed?
end
