set datafile separator ','
set key autotitle columnhead
set ylabel 'amount'
set xlabel 'round'

set terminal pngcairo size 1920,1080 enhanced font 'Segoe UI,10'
set output 'metrics.png'

plot 'metrics.csv' using 1:2 with lines, '' using 1:3 with lines, '' using 1:4 with lines

