# EuroCob 
EuroMillions combinations calculator, using what I know of probabilities I try to reduce the number of combinations.

------------
## Features :tw-1f680:

### Combinations
Using [itertools](https://docs.python.org/3/library/itertools.html "itertools") I calculate all the combinations.

### Probabilidad
1. Eliminated consecutive combinations
2. Eliminate the combinations that all numbers are even and odd
3. Eliminate the combinations that have a very small difference between the numbers

    (k[3]+k[4])-(k[0]+k[1])=c
    c/k[2]= x
    x>`difference`

## To do
- [ ] Extract the winning numbers from a website
   - [ ] Sort the numbers according to times they have come out
- [ ] Sift combination according to the table of numbers obtained above.

## How Can I Support This?
The easiest thing you can do is give me a star.
If you have a suggestion, Fork the `master` branch and open a Pull Request.
## Thanks For Reading!
