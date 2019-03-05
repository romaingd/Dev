require 'test_helper'

class SessionsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @user = users(:one)
  end

  test "should get new" do
    get login_path
    assert_response :success
  end

  test "should log in" do
    post login_path, params: { session: { email: @user.email, password: 'secret' } }
    assert_equal session[:user_id], @user.id
  end

  test "should log in then log out" do
    post login_path, params: { session: { email: @user.email, password: 'secret' } }
    assert_equal session[:user_id], @user.id
    delete logout_path
    assert_not_equal session[:user_id], @user.id
  end

  test "should login created user" do
    post users_url, params: { user: { name: 'foo2', email:'foo2@example.com', password: 'foo', password_confirmation: 'foo' } }

    user = User.last

    assert_redirected_to user_url(user)
    assert_equal user.id, session[:user_id]
  end

end
