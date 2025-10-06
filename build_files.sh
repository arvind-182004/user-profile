
echo "🔧 Installing dependencies..."
python3.12 -m pip install -r requirements.txt

echo "📦 Running collectstatic..."
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput
# python3.12 manage.py collectstatic --noinput

echo "✅ Build complete!"
