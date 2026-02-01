echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setting up database..."
mysql -u root < sql/schema.sql

echo "Setup complete!"
