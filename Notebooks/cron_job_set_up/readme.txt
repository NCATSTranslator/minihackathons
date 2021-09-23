Currently the submit.sh is set up as a cron job for daily 4pm through Monday-Thursday and Sunday.
Note currently submitting 42 queries to ARS prod through ARAX prod for synchronous queries and similar for asynchronous except through ARS dev. Asynchronous is only set up for bte Aragorn and arax... the time gap between each submission for Asynchronous is ~9 minutes and total ~ 6 hours. 
For synchronous queries ~12 minutes gap between each workflow and total of ~ 8 hours. The whole pipeline approximately takes 15 hours...


0 16 * * 0-4 sample.sh 1>/dev/null 2>&1


you can switch to daily 9pm. E.g. 

0 21 * * * sample.sh 1>/dev/null 2>&1