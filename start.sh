cd /home/pi/mnt/albioncsoda ;
python3 dlandconvertocsv.py  > dlresults.txt
python3 print_me_what_to_Craft.py >results.txt
git add dlresults.txt
git add results.txt
git commit -m "automated update"
git push origin master

