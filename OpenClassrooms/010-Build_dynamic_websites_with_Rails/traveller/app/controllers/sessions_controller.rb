class SessionsController < ApplicationController
  def new
  end

  def create
    user = User.find_by(email: params[:session][:email])

    if user && user.authenticate(params[:session][:password])
      login(user)
      redirect_to user
    else
      flash.now[:danger] = 'Bad email/password combination. Try again.'
      render 'new'
    end
  end

  def destroy
    logout
    redirect_to site_home_path
  end
end
