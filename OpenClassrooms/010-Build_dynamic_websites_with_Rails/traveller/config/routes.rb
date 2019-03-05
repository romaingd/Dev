Rails.application.routes.draw do
  get 'sessions/new'
  get 'site/home'

  get '/login', to: 'sessions#new'
  post '/login', to: 'sessions#create'
  delete '/logout', to: 'sessions#destroy'

  resources :posts
  resources :users


  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
