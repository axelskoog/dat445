
sed -n 's/^  \* \([^[].*\)$/\1/p' README.md |
while read -r line
do
	exercise=$(printf '%s' "$line" | sed -e 's| [(]exam[)]$||' -e 's| |_|g')
	link=$(find ./Uppgifter -name '*_'"$exercise"'*.md')
	if test -f "${link:--}"; then
		sed -i '/^  \* '"$line"'$/ s|'"$line"'|['"$line"']('"$link"')|' README.md
	fi
done
