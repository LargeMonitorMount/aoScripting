cd /home/pi/mnt/albioncsoda ;
python3 dlandconvertocsv.py  > dlresults.txt
python3 print_me_what_to_Craft.py >results.csv
git add dlresults.txt
git add results.csv
git commit -m "automated update"
git push origin master

