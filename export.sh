#This script exports only the files needed to port the bot to another host.
echo -e "Please input the target folder"
read target
mkdir $target
xargs -a manifest.txt cp -t $target
