echo "-------------------------------------------"
echo -e "\t Liste des fichiers"
echo "-------------------------------------------"

echo " Entrez le nom du dossier : "
read dd
cpath=$(pwd)
fullpath=$cpath$"/"$dd
if [ -d $dd ]
then
for i in $(ls $fullpath)
do 
	echo $i
done
else
	echo "$dd n'est pas un fichier."
fi

#j'ai pas réussi à afficher un message quand il y a plus de 10 fichiers