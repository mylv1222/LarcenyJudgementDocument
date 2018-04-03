@echo off
echo pwd: %cd%
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo git add start
git add -A .
echo git add done
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo git commit start
git commit -m "%date% %time%"
echo git commit done
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo git push start
git push https://git.coding.net/milesgu/LarcenyJudgementDocument
echo git push done
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo all done!
echo;

pause