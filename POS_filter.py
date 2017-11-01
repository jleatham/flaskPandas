#!/usr/bin/python3
#----------#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3   #for work laptop

## crontab -e
## * * * * * /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 /Users/jleatham/Documents/Programming/Python/automation/POS/v3_pos_automation.py
## if it doesn't edit, type 'export EDITOR=VIM' in terminal
## make python file executable with chmod a+x
## Example crontab :
##    ###Every 10 minutes, check for new CSV by running filter python program
##    */10 * * * * /usr/bin/python3 /home/cisco/houston-pos/v9_POS_filter.py
##    ###first of every month, move CSV data to monthly csv, remove old POS files
##    0 0 1 * * /usr/bin/python3 /home/cisco/houston-pos/v9_POS_upload.py
##    ###makesure http-server is running after reboot
##    @reboot http-server /home/cisco/houston-pos/

from POS_automation import * #includes list of accounts and am names to search, as well as variables to import



#################Start main


try:
    if (sys.argv[1] == "test"):
        prepare_test()
    elif (sys.argv[1] == "upload"):
        print("upload argv")
        #added these two functions below, probably don't need to set a seperate command for these
        create_monthly_csv(all_data_csv_filename)
        create_html_tables()
        #send_link_to_spark(roomId)

except Exception as e:
    pass
    #print ("Problem with argv ")
    #print (e)

file_index = []    
for file in glob.glob(home_file_path + '/*.[Cc][Ss][Vv]'):
    file_index.append(file)


#create html table using csvtotable, installed on ubuntu server
if file_index:
    to_csv_from_json_v1(file_index,all_data_csv_filename, non_error_pos_data_filename)
    print ("all files processed")
    to_html_v1(all_data_csv_filename,all_data_html_filename)
    create_monthly_csv(all_data_csv_filename)
    create_html_tables()

else:
    #print("no new files to process")
    sys.exit(0)
    #check_mbr_v1(329284198)
####################End main