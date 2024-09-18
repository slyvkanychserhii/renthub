# ---------------------------------------------------------------------

# Reset the current branch to the commit just before the last 12:
# git reset --hard HEAD~12

# HEAD@{1} is where the branch was just before the previous command.
# This command sets the state of the index to be as it would just
# after a merge from that commit:
# git merge --squash HEAD@{1}

# Commit those squashed changes.  The commit message will be helpfully
# prepopulated with the commit messages of all the squashed commits:
# git commit


# git push --force origin main


# git rm --cached myfile.txt
# git rm -r --cached mydir

# ---------------------------------------------------------------------

# docker-compose up               # Запускает контейнеры
# docker-compose up -d            # Запускает контейнеры в фоновом режиме
# docker-compose stop             # Останавливает контейнеры
# docker-compose down             # Останавливает и удаляет контейнеры, сети и образы (тома не удаляются)
# docker-compose down --volumes   # Останавливает и удаляет контейнеры, сети, образы и тома
# docker-compose restart          # Перезапускает контейнеры

# python manage.py migrate
# python manage.py makemigrations
# python manage.py createsuperuser
# python manage.py runserver
# python manage.py collectstatic

# ---------------------------------------------------------------------

''' Скрипт для развертываания на AWS

#!/bin/bash
dnf update -y
amazon-linux-extras enable docker
dnf install -y docker
systemctl start docker
systemctl enable docker
usermod -aG docker $USER
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
dnf install -y git
cd /opt/
git clone https://github.com/it-career-hub/example-voting-app.git
cd example-voting-app
docker-compose up -d

'''

# ---------------------------------------------------------------------
