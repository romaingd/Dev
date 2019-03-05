class User < ApplicationRecord
  has_many :posts, dependent: :destroy

  validates :name, presence: true
  EMAIL_FORMAT = /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i
  validates :email, presence: true, format: { with: EMAIL_FORMAT }, uniqueness: true

  before_save { self.email = email.downcase }

  has_secure_password

  has_attached_file :avatar, styles:{ medium: "300x300", thumb: "100x100"}, default_url: ".images/:style/missing.png"
  validates_attachment_content_type :avatar, content_type: /\Aimage\/.*\z/

end
