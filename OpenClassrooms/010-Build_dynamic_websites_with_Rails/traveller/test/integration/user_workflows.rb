require 'test_helper'
  
class UserWorkflowsTest < ActionDispatch::IntegrationTest
  setup do
    @user = users(:one)
  end 
    
  test "after logging in, a user can edit their posts" do
    post login_path, params: { session: { email: @user.email, password: 'secret' } }
    get post_path(@user.posts.first)
    assert_response :success
    patch post_path(@user.posts.first), params: { post: { title: "change" } }
    assert_equal @user.posts.first.title, "change"
    assert_redirected_to post_url(@user.posts.first)
  end
end