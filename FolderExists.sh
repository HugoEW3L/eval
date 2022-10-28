echo "-----------------------------------------------------"
echo -e "\t Nous regardons si le dossier existe"
echo "-----------------------------------------------------"
echo "Entrez le nom du dossier : "
read dd
if [ -d $dd ]
then
	echo "$dd Le dossier existe !"
else
	echo "$dd Le dossier n'existe pas."
fi
