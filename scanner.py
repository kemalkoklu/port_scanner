import socket
import os

def availabilty(ip):
    try:
        response = os.system(f"ping -c 1 {ip}")
        if response == 0:
            return True

        else:
            return False
    except Exception as err:
        return False

def scan_host(start_of_range,end_of_range):
    
    port_dic = {}# dictionary for storing which port got which result
    err_dic = {} # dictionary for storing which port got error
    socket.setdefaulttimeout(0.5) # setting timeout value
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # creating socket for scan
    ip = socket.gethostbyname(socket.gethostname()) #getting machine's local ip
    
    for port in range(start_of_range,end_of_range): # for loop for scanning each port value between given range
        try:

        
                result = sock.connect_ex((ip,port))
                port_dic[port] = result


        except Exception as Err:
            err_dic[port] = Err

        
    port_dic[port] = result
    between_list = [] # storing which port ranges was succesful
    success_start = 1 # first succesful port of that range
    end_success = 1 # last successful port
    bool_first_err = True
    for key in  port_dic.keys():
        if port_dic[key] == 0 and bool_first_err==True:
            end_success +=1

        elif port_dic[key] == 0 and bool_first_err == False:
            end_success +=1
            start_of_range = end_success

        elif port_dic[key] != 0 and bool_first_err == True: # after first  succesful range detects that port which got an error
            bool_first_err == False
            between_list.append(f"{success_start}-{end_success}")
            success_start = end_success+1

        elif port_dic[key] != 0 and bool_first_err == False:
            success_start +=1
    
    between_list.append(f"{success_start}-{end_success}")

    for succ in between_list:
        print("port: "+succ + " Successful")

    for key in err_dic.keys():
        err_dic["key"]
        print(f"port: {key}  err:{err_dic[key]}")





def scan_network(ip_range,start_of_range,end_of_range): # scans 1 or more than 1 ip with ports in local network
    port_dic = {} # dictionary for storing which port got which result
    err_dic = {} # dictionary for storing which port got error
    socket.setdefaulttimeout(1)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

     
    strr = ""
        
    if type(ip_range) == type(strr):
            avaible = availabilty(ip_range)

            if avaible == True:
                pass
            elif avaible == False:
                return 

            for port in range(start_of_range,end_of_range): # for loop for scanning each port value between given range
                try:

                
                    result = sock.connect_ex((ip_range,port))
                    port_dic[port] = result


                except Exception as Err:
                    err_dic[port] = Err

            
            
            between_list = [] # storing which port ranges was succesful
            success_start = 1 # first succesful port of that range
            end_success = 1 # last successful port
            bool_first_err = True
            for key in  port_dic.keys():
                if port_dic[key] == 0 and bool_first_err==True:
                    end_success +=1

                elif port_dic[key] == 0 and bool_first_err == False:
                    end_success +=1
                    start_of_range = end_success

                elif port_dic[key] != 0 and bool_first_err == True: # after first  succesful range detects that port which got an error
                    bool_first_err == False
                    between_list.append(f"{success_start}-{end_success}")
                    success_start = end_success+1

                elif port_dic[key] != 0 and bool_first_err == False:
                    success_start +=1
        
            between_list.append(f"{success_start}-{end_success}")

            for succ in between_list:
                print("port :" +succ + " Successful")

            for key in err_dic.keys():
                err_dic[key]
                print(f"port: {key}  err:{err_dic[key]}")
        
    
    else:
        print("please enter a valid ip address")
        return

