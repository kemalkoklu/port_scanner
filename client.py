from scanner import scan_network,scan_host

if __name__ == "__main__":




    print('''    $$$$$$$\   $$$$$$\  $$$$$$$\ $$$$$$$$\        $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\ $$$$$$$\                
    $$  __$$\ $$  __$$\ $$  __$$\\__$$  __|       $$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |$$$\  $$ |$$  _____|$$  __$$\               
    $$ |  $$ |$$ /  $$ |$$ |  $$ |  $$ |         $$ /  \__|$$ /  \__|$$ /  $$ |$$$$\ $$ |$$$$\ $$ |$$ |      $$ |  $$ |              
    $$$$$$$  |$$ |  $$ |$$$$$$$  |  $$ |         \$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |$$$$$\    $$$$$$$  |              
    $$  ____/ $$ |  $$ |$$  __$$<   $$ |          \____$$\ $$ |      $$  __$$ |$$ \$$$$ |$$ \$$$$ |$$  __|   $$  __$$<               
    $$ |      $$ |  $$ |$$ |  $$ |  $$ |         $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$ |              
    $$ |       $$$$$$  |$$ |  $$ |  $$ |         \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$ |$$$$$$$$\ $$ |  $$ |              
    \__|       \______/ \__|  \__|  \__|          \______/  \______/ \__|  \__|\__|  \__|\__|  \__|\________|\__|  \__|              
                                                                                                                                 
                                                                                                                                 
                                                                                                                                 
    $$$$$$$\ $$\     $$\       $$\   $$\ $$$$$$$$\ $$\      $$\  $$$$$$\  $$\       $$\   $$\  $$$$$$\  $$\   $$\ $$\      $$\   $$\ 
    $$  __$$\\$$\   $$  |       $$ | $$  |$$  _____|$$$\    $$$ |$$  __$$\ $$ |      $$ | $$  |$$  __$$\ $$ | $$  |$$ |     $$ |  $$ |
    $$ |  $$ |\$$\ $$  /       $$ |$$  / $$ |      $$$$\  $$$$ |$$ /  $$ |$$ |      $$ |$$  / $$ /  $$ |$$ |$$  / $$ |     $$ |  $$ |
    $$$$$$$\ | \$$$$  /        $$$$$  /  $$$$$\    $$\$$\$$ $$ |$$$$$$$$ |$$ |      $$$$$  /  $$ |  $$ |$$$$$  /  $$ |     $$ |  $$ |
    $$  __$$\   \$$  /         $$  $$<   $$  __|   $$ \$$$  $$ |$$  __$$ |$$ |      $$  $$<   $$ |  $$ |$$  $$<   $$ |     $$ |  $$ |
    $$ |  $$ |   $$ |          $$ |\$$\  $$ |      $$ |\$  /$$ |$$ |  $$ |$$ |      $$ |\$$\  $$ |  $$ |$$ |\$$\  $$ |     $$ |  $$ |
    $$$$$$$  |   $$ |          $$ | \$$\ $$$$$$$$\ $$ | \_/ $$ |$$ |  $$ |$$$$$$$$\ $$ | \$$\  $$$$$$  |$$ | \$$\ $$$$$$$$\\$$$$$$  |
    \_______/    \__|          \__|  \__|\________|\__|     \__|\__|  \__|\________|\__|  \__| \______/ \__|  \__|\________|\______/ 
                                                                                                                                 
                                                                                                                                 ''')


    

    while True:
        menu = int(input(" 1: host scan  \n 2: network_scan "))
        if menu < 1 or menu > 2:
            print("invalid value")
            continue 

        match menu:
            case 1:
                start = int(input(" start port cant be lower than 1 \n enter start port "))
                end = int(input(" end port cant be lower than 65535 \n enter end port "))
                scan_host(start, end)
            case 2:
                start = int(input(" start port cant be lower than 1 \n enter start port "))
                end = int(input(" end port cant be lower than 65535 \n enter end port "))

                ip = str(input(" for example 172.168.1.231 \n enter ip:"))

                scan_network(ip,start,end)
            case 3:
                start = int(input(" start port cant be lower than 1 \n enter start port "))
                end = int(input(" end port cant be lower than 65535 \n enter end port "))
                ip_arr = []
                ip_count = int(input("how much ip address do you want to enter"))
                for count in range(0,ip_count):
                    ip_arr.append(str(input(f"enter port address{count+1}")))
