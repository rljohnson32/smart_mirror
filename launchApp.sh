cd /home/pi/mirror/capstone_gui
#python -m SimpleHTTPServer 8000 &
sudo killall mini-httpd
sudo mini-httpd -c "/home/pi/mirror/capstone_gui/cgi-bin/*" &
sudo chromium-browser --no-sandbox --disable-infobars http://localhost/html/index.html --start-fullscreen
