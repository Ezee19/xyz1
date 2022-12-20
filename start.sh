if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning https://github.com/Ezee19/xyz.git /xyz
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /xyz
fi
cd /xyz
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
