json.extract! user, :id, :provider, :uid, :name, :mail, :image_url, :created_at, :updated_at
json.url user_url(user, format: :json)
