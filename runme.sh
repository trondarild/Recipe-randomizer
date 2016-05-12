cd ~/Kode/Python/reciperandomizer/
python reciperandomizer.py -f "oppskrifter kjøtt sverige.txt,oppskrifter kylling.txt,oppskrifter fisk.txt,oppskrifter vegetar.txt" -n "2,2,2,1" -exclude "exclude.txt" -category "kategorier.txt" > ukemeny.txt
cp ukemeny.txt ~/Dropbox/
echo ukemeny.tx. is in ~/Dropbox/
