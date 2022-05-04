Rails.application.routes.draw do
  # Resources
  resources :users, only: %i[index show destroy]

  get 'top/index'
  root 'top#index'
  get '/login', to: 'login#index'
  get '/auth/logout'
  # Add route for OmniAuth callback
  match '/auth/:provider/callback', :to => 'auth#callback', :via => [:get, :post]
end
