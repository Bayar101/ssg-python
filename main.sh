python3 src/main.py
cd public
python3 -m http.server 8888 &
sleep 1
open http://localhost:8888
wait
