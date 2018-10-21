##打开终端输入以下命令:
 - git clone https://github.com/MTxZz/webchat
 - virtualenv Dj  --no-site-packages
 - source ./Dj/bin/activate
 - pip install -r requirements.txt
 - python manage.py migrate
 - python manage.py createsuperuser
 - python manage.py run_chat_server

##打开新的终端，接着输入，前一个终端不要关
 - python manage.py runserver
##打开浏览器访问
 - 127.0.0.1：8000
