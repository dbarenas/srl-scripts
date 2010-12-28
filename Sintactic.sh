NOW=$(pwd)
EXT="/home/darenas/TESIS/tools/POS/CollinsParser/COLLINS-PARSER"
tagged="corpus/sav.tagged"
parsed="corpus/sav.parsed"

cd $EXT
pwd
./Collins $NOW/$tagged  
cd $NOW
pwd
