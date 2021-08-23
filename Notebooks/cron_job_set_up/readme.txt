Currently the submit.sh is set up as a cron job for daily 9pm through Monday-Thursday and Sunday. 


0 21 * * 0-4 sample.sh 1>/dev/null 2>&1


you an switch to daily 9pm. E.g. 

0 21 * * * sample.sh 1>/dev/null 2>&1