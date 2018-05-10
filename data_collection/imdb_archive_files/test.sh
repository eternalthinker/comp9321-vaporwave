
grep tt0944947 data.tsv | while read cols
do
	epId=`echo $cols | cut -d' ' -f1`
	echo -e "${cols}\t`grep $epId ../title.basics.tsv/data.tsv`\t`grep $epId ../title.ratings.tsv/data.tsv | cut -d' ' -f2-`" | cut -d$'\t' -f3,4,7,10,12,15,16
done
